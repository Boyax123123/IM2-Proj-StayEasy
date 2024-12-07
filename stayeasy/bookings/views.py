from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from stayeasy.views import date_test  # Custom date for testing
from bookings.models import Bookings
from reviews.models import Reviews  # Import Reviews model
import json

@login_required(login_url='accounts:login')
def my_bookings(request):
    if request.user.role != 'customer':
        return redirect('restricted')

    # Use custom date if provided; otherwise, use today's date
    current_date = date_test or date.today()

    # Fetch bookings for the current user
    all_bookings = Bookings.objects.filter(customer=request.user).order_by('-booking_date')

    # Categorize bookings based on their status and dates
    current_bookings = all_bookings.filter(
        status__in=['pending', 'confirmed'],
        checkout_date__gte=current_date,
    )
    future_bookings = all_bookings.filter(
        checkin_date__gt=current_date,
        status='confirmed',
    )
    completed_bookings = all_bookings.filter(status='completed')
    cancelled_bookings = all_bookings.filter(status='cancelled')

    # Retrieve all reviews for the user's bookings
    user_reviews = Reviews.objects.filter(customer=request.user)
    reviewed_booking_ids = set(review.booking.id for review in user_reviews)  # Extract booking IDs with reviews

    # Add a "can_cancel" flag for current bookings
    for booking in current_bookings:
        if booking.status == "pending":
            booking.can_cancel = True
        elif booking.status == "confirmed" and booking.checkin_date > current_date:
            booking.can_cancel = True
        else:
            booking.can_cancel = False

    context = {
        'current_bookings': current_bookings,
        'all_bookings': all_bookings,
        'future_bookings': future_bookings,
        'completed_bookings': completed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'today': current_date,
        'reviewed_booking_ids': reviewed_booking_ids,  # Pass only reviewed booking IDs
    }
    return render(request, 'bookings/my_bookings.html', context)


@login_required(login_url='accounts:login')
def cancel_booking(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            booking_id = data.get("booking_id")

            # Fetch the booking for the current user
            booking = get_object_or_404(Bookings, id=booking_id, customer=request.user)

            # Handle cancellation logic
            if booking.status == "pending":
                # If pending, directly cancel the booking
                booking.status = "cancelled"
                booking.save()
                return JsonResponse({"success": True, "message": "Booking has been canceled."})

            elif booking.status == "confirmed" and booking.checkin_date > date.today():
                # If confirmed and check-in date is in the future, cancel and refund
                request.user.balance += booking.total_cost
                request.user.save()
                booking.status = "cancelled"
                booking.save()
                return JsonResponse({"success": True, "message": "Booking has been canceled and refunded."})

            else:
                # Booking cannot be canceled
                return JsonResponse({"success": False, "message": "This booking cannot be canceled."})

        except Bookings.DoesNotExist:
            # Booking does not exist for the current user
            return JsonResponse({"success": False, "message": "Booking not found."})

        except Exception as e:
            # Catch other exceptions
            return JsonResponse({"success": False, "message": str(e)})

    # Invalid request method
    return JsonResponse({"success": False, "message": "Invalid request method."})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from datetime import datetime
from bookings.models import Bookings 


def landingpage(request):
    return render(request, 'stayeasy/landingpage.html')


def restricted(request):
    return render(request, 'stayeasy/restricted.html')



@login_required
def add_funds(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount", 0))
            if amount <= 0:
                messages.error(request, "Amount must be greater than 0.")
                return redirect("wallet")  # Replace with your wallet page URL name

            # Update user's balance
            user = request.user
            user.balance += amount
            user.save()
            messages.success(request, f"₱{amount} has been added to your wallet.")
        except ValueError:
            messages.error(request, "Invalid amount.")
    
    return redirect("wallet")


 # Import the Bookings model



# Global variable to store the test date
date_test = None

def set_test_date(request):
    global date_test  # Declare the global variable

    if request.method == "POST":
        # Get the test date from the request
        test_date = request.POST.get('test_date')

        if not test_date:  # Check if the test_date is blank or None
            # If blank, reset to the current date
            test_date = datetime.today().date().isoformat()

        # Store the test date in the session and update the global variable
        request.session['test_date'] = test_date
        date_test = datetime.strptime(test_date, '%Y-%m-%d').date()

        # Auto-update booking instances
        update_booking_status(date_test)

    return redirect(request.META.get('HTTP_REFERER', '/'))

def update_booking_status(current_date):
    bookings = Bookings.objects.all()
    for booking in bookings:
        if booking.status == 'pending' and booking.checkin_date < current_date:
            booking.status = 'cancelled'
            booking.save()
        elif booking.status == 'confirmed' and booking.checkout_date < current_date:
            booking.status = 'completed'
            booking.save()
        elif booking.status == 'completed' and booking.checkin_date <= current_date <= booking.checkout_date:
            booking.status = 'confirmed'
            booking.save()
        elif booking.status == 'cancelled':
            continue



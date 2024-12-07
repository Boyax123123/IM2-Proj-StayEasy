from django.shortcuts import render, redirect, get_object_or_404
from properties.models import Property
from .models import Reviews
from bookings.models import Bookings
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def add_review(request, property_id, booking_id):
    # Fetch the property and booking
    property = get_object_or_404(Property, id=property_id)
    booking = get_object_or_404(Bookings, id=booking_id)

    # Check if a review already exists for this booking
    existing_review = Reviews.objects.filter(property=property, booking=booking, customer=request.user).first()

    if request.method == 'POST':
        if existing_review:
            # If a review exists, update it
            form = ReviewForm(request.POST, instance=existing_review)
        else:
            # If no review exists, create a new one
            form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.property = property
            review.booking = booking
            review.save()
            return redirect('properties:property_details', property_id=property.id)
    else:
        if existing_review:
            # Pre-fill the form with the existing review
            form = ReviewForm(instance=existing_review)
        else:
            # Display an empty form for a new review
            form = ReviewForm()

    context = {
        'property': property,
        'form': form,
        'existing_review': existing_review,  # Pass this to check in the template
    }
    return render(request, 'reviews/add_review.html', context)




def property_reviews(request, property_id):
    # Get the property object
    property = get_object_or_404(Property, id=property_id)

    # Fetch all reviews for the property
    reviews_list = Reviews.objects.filter(property=property).order_by('-review_date')

    # Count the total number of reviews
    reviews_count = reviews_list.count()

    # Pagination: Show 5 reviews per page
    paginator = Paginator(reviews_list, 5)
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    # Pass data to the template
    context = {
        'property': property,
        'reviews': reviews,
        'reviews_count': reviews_count,  # Add the total reviews count
    }

    return render(request, 'reviews/property_reviews.html', context)
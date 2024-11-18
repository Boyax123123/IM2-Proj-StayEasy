from django.shortcuts import render, redirect, get_object_or_404
from properties.models import Property
from .models import Reviews
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts


def add_review(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    # Initialize form for review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Manually handle user and property id for testing if provided in form data
            user_id = request.POST.get('user_id')  # Testing purposes
            property_id = request.POST.get('property_id')  # Testing purposes
            
            # Create the review instance but don't save yet
            review = form.save(commit=False)
            review.user = request.user if not user_id else Accounts.objects.get(id=user_id)
            review.property = property if not property_id else Property.objects.get(id=property_id)
            
            # Save the review to the database
            review.save()
            return redirect('property:property_detail', property_id=property.id)
    else:
        form = ReviewForm()

    context = {
        'property': property,
        'form': form,
    }
    return render(request, 'reviews/add_review.html', context)

def review_list(request):
    # Your logic for fetching and displaying reviews
    return render(request, 'reviews/review.html')


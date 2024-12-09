# properties views;
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm
from .models import Property, Wishlist
from reviews.models import Reviews
from accounts.models import Accounts
from bookings.models import Bookings 
from reviews.models import Reviews
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import json
from django.utils.timezone import now
from django.db.models import QuerySet
from django.db.models import Q



#propertydetail==========================

def property_details(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    user = request.user

    # Fetch unavailable dates
    bookings = Bookings.objects.filter(property=property, status__in=['pending', 'confirmed'])
    unavailable_dates = []
    for booking in bookings:
        current_date = booking.checkin_date
        while current_date <= booking.checkout_date:
            unavailable_dates.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)

    # Fetch booking information for the user
    user_bookings = []
    if user.is_authenticated:
        user_bookings = Bookings.objects.filter(
            customer=user,
            property=property,
            status__in=['pending', 'confirmed']
        )

    # Prepare the booking status message
    booking_status_message = None
    active_booking = user_bookings.filter(checkin_date__lte=datetime.now().date(), checkout_date__gte=datetime.now().date()).exists()
    future_bookings_count = user_bookings.filter(checkin_date__gt=datetime.now().date(), status='confirmed').count()
    pending_booking = user_bookings.filter(status='pending').exists()

    if active_booking:
        booking_status_message = "Currently Booked: Your stay is in progress."
    elif future_bookings_count > 0:
        booking_status_message = f"Future Bookings: {future_bookings_count}"
    elif pending_booking:
        booking_status_message = "Booked: Pending Host Approval."
    elif user_bookings.exists():
        booking_status_message = "Property Booked"

    # Fetch reviews for the property
    reviews = Reviews.objects.filter(property=property).order_by('-review_date')[:2]

    # Handle booking submission
    if request.method == 'POST':
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        total_cost = request.POST.get('total_cost')

        checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d').date()
        checkout_date = datetime.strptime(checkout_date, '%Y-%m-%d').date()

        # Save booking to the database
        booking = Bookings.objects.create(
            customer=user,
            property=property,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            total_cost=total_cost,
            status='pending'
        )

        return JsonResponse({'message': 'Booking successful!', 'booking_id': booking.id})

    return render(request, 'properties/property.html', {
        'property': property,
        'unavailable_dates': unavailable_dates,
        'booking_status_message': booking_status_message,
        'reviews': reviews,
    })

def booking_create(request):
    if request.method == 'POST':
        # Extract data from the request
        customer = request.user  # The currently logged-in user
        property_id = request.POST.get('property_id')
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        total_cost = float(request.POST.get('total_cost'))

        # Convert dates to Python date objects
        checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d').date()
        checkout_date = datetime.strptime(checkout_date, '%Y-%m-%d').date()

        # Check if user balance is sufficient
        if customer.balance < total_cost:
            return JsonResponse({
                'status': 'error',
                'message': 'Insufficient balance. Please top up your wallet to proceed with the booking.'
            }, status=400)

        # Fetch the property
        property = get_object_or_404(Property, id=property_id)

        # Check for overlapping bookings for any user
        overlapping_bookings = Bookings.objects.filter(
            property=property,
            status__in=['pending', 'confirmed'],  # Only consider active bookings
        ).filter(
            checkin_date__lt=checkout_date,  # Check-in date overlaps
            checkout_date__gt=checkin_date   # Check-out date overlaps
        )

        if overlapping_bookings.exists():
            return JsonResponse({
                'status': 'error',
                'message': 'The property is already booked for the selected dates. Please choose different dates.'
            }, status=400)

        # Check for overlapping bookings for the same user
        overlapping_user_bookings = Bookings.objects.filter(
            customer=customer,
            property=property,
            status__in=['pending', 'confirmed'],
            checkin_date__lt=checkout_date,  # Check-in date overlaps
            checkout_date__gt=checkin_date   # Check-out date overlaps
        )

        if overlapping_user_bookings.exists():
            return JsonResponse({
                'status': 'error',
                'message': 'You already have a booking that overlaps with the selected dates. Please choose different dates.'
            }, status=400)

        # Create the booking
        booking = Bookings.objects.create(
            customer=customer,
            property=property,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            total_cost=total_cost,
            status='pending'  # Default status
        )

        # Deduct the amount from the customer's balance
        customer.balance -= total_cost
        customer.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Booking created successfully!',
            'booking_id': booking.id
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

# def property_details(request, property_id):
#     property = get_object_or_404(Property, id=property_id)  # Fetch the property with the given ID
#     return render(request, 'properties/property.html', {'property': property})

# ........
# @login_required
# def property_details(request, property_id):
#     # Fetch the property with the given ID
#     property = get_object_or_404(Property, id=property_id)
    
#     # Wishlist functionality
#     wishlist = Wishlist.objects.filter(user=request.user, properties=property).first()
    
#     # Handling form submission for wishlist
#     if request.method == 'POST':
#         if 'add_to_wishlist' in request.POST:
#             # Add property to wishlist
#             wishlist, created = Wishlist.objects.get_or_create(user=request.user)
#             wishlist.properties.add(property)
#         elif 'remove_from_wishlist' in request.POST:
#             # Remove property from wishlist
#             wishlist.properties.remove(property)
        
#         # After handling wishlist action, reload the page
#         return redirect('properties:property_details', property_id=property.id)
    
#     # Review functionality
#     reviews = Reviews.objects.filter(property=property)
    
#     if request.method == 'POST' and 'submit_review' in request.POST:
#         review_content = request.POST.get('review_content')
#         if review_content:
#             # Add the review
#             Reviews.objects.create(
#                 property=property,
#                 user=request.user,
#                 content=review_content,
#                 created_at=datetime.now()
#             )
#             # Reload the page after review submission
#             return redirect('properties:property_details', property_id=property.id)

#     # Bookings functionality (optional, depends on your use case)
#     if request.method == 'POST' and 'book_property' in request.POST:
#         checkin_date = request.POST.get('checkin_date')
#         checkout_date = request.POST.get('checkout_date')
        
#         if checkin_date and checkout_date:
#             booking = Bookings.objects.create(
#                 user=request.user,
#                 property=property,
#                 checkin_date=checkin_date,
#                 checkout_date=checkout_date,
#                 total_cost=request.POST.get('total_cost')  # Assuming you calculate total cost client-side
#             )
#             return redirect('properties:booking_confirmation', booking_id=booking.id)
    
#     # Unavailable dates (just an example, you might get this from bookings)
#     unavailable_dates = Bookings.objects.filter(property=property).values_list('checkin_date', flat=True)

#     # Return the property details along with other relevant context
#     return render(request, 'properties/property.html', {
#         'property': property,
#         'wishlist': wishlist,
#         'reviews': reviews,
#         'unavailable_dates': unavailable_dates,
#     })

#host property page

@login_required(login_url="/accounts/login/")
def host_property(request):

    if request.user.role != 'host':
        return redirect('restricted')
    context = {}
    user = request.user
    text = ''
   
    host = user
    if 'sortPriceHigher' in request.POST:
        properties = Property.objects.filter(host=host).order_by('-price')
    elif'sortPriceLower' in request.POST:
        properties = Property.objects.filter(host=host).order_by('price')  
    elif 'sortAlpha' in request.POST:
        text = 'Sorted Alphabetically'
        properties = Property.objects.filter(host=host).order_by('name')
    elif 'sortRating' in request.POST:
        properties = Property.objects.filter(host=host).order_by('-rating')
    else:
        properties = Property.objects.filter(host=host)


    if 'deleteProperty' in request.POST:
        pk = request.POST.get('deleteProperty')
        property = Property.objects.get(id = pk)
        property.delete()
    

    context['pressed'] = text
    context['properties'] = properties
    return render(request, 'properties/myProperties.html', context)

# def create_property(request, pk = None):
#     if pk:
#         property_instance = get_object_or_404(Property, pk=pk)
#         form = PropertyForm(request.POST or None, instance=property_instance)
#     else:
#         # Otherwise, create a new property
#         form = PropertyForm(request.POST or None)
    
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('properties:property_list')  # Redirect after form submission
    
    return render(request, 'properties/create_property.html', {'form': form})
def create_property(request, pk = None):
    if request.user.role != 'host':
        # Add an error message to be shown in the template
        messages.error(request, 'You must be a host to create a property.')
        return redirect('landingpage')  
    if pk:
        property_instance = get_object_or_404(Property, pk=pk)
        form = PropertyForm(request.POST or None, instance=property_instance)
   
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.host = request.user
            form.save()
            return redirect('properties:my_properties')
    else:
        form = PropertyForm()

    return render(request, 'properties/create_property.html', {'form': form})

# if request.user.is_authenticated:
#     form.instance.host = request.user
# else:
#     form.add_error('host', 'You must be logged in to create a property.')

def host_dashboard(request):
    return render(request, 'properties/host_dashboard.html')



@csrf_exempt
@csrf_exempt
def listing(request):
    user = request.user  # Refers to the currently logged-in Accounts user
    context = {}

    # Handle wishlist for authenticated users
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(account=user)
        wishlisted_properties = wishlist.property.all()  # Get all properties in this user's wishlist
    else:
        wishlisted_properties = Property.objects.none()  # Empty queryset for unauthenticated users

    # Default to displaying all properties
    properties = Property.objects.all()
    sort_type = "default"  # Default sorting type
    search_query = request.POST.get('searchQuery', '').strip()  # Get search query from form

    # Handle Add to Wishlist
    if "add_to_wishlist" in request.POST and request.user.is_authenticated:
        property_id = request.POST.get("add_to_wishlist")
        property_to_add = Property.objects.get(id=property_id)
        wishlist, created = Wishlist.objects.get_or_create(account=user)
        wishlist.property.add(property_to_add)

    # Handle Remove from Wishlist
    if "remove_from_wishlist" in request.POST and request.user.is_authenticated:
        property_id = request.POST.get("remove_from_wishlist")
        property_to_remove = Property.objects.get(id=property_id)
        wishlist = Wishlist.objects.get(account=user)
        wishlist.property.remove(property_to_remove)

    # Search logic
    if search_query:
        if search_query.isdigit():  # If the search query is numeric
            number = int(search_query)
            # Determine the range
            if number < 1000:  # If input is in the hundreds
                range_start = number
                range_end = range_start + 99
            else:  # If input is in the thousands
                range_start = number
                range_end = range_start + 999

            # Filter properties by price within the range
            properties = properties.filter(price__gte=range_start, price__lte=range_end)
        else:
            # Filter properties by name or address containing the search term
            properties = properties.filter(
                Q(name__icontains=search_query) | Q(address__icontains=search_query)
            )

    # Sorting logic (applies to filtered results if a search query exists)
    if "sortPriceHigher" in request.POST:
        properties = properties.order_by('-price')
        sort_type = "price_high"
    elif "sortPriceLower" in request.POST:
        properties = properties.order_by('price')
        sort_type = "price_low"
    elif "sortAlpha" in request.POST:
        properties = properties.order_by('name')
        sort_type = "alpha"
    elif "sortRating" in request.POST:
        properties = properties.order_by('-rating')
        sort_type = "rating"

    # Pass data to the template
    context['properties'] = properties
    context['wishlists'] = wishlisted_properties
    context['sort_type'] = sort_type
    context['is_authenticated'] = request.user.is_authenticated
    context['search_query'] = search_query  # Pass search query back to the template
    return render(request, 'properties/listing.html', context)


    # Pass data to the template
    context['properties'] = properties
    context['wishlists'] = wishlisted_properties
    context['sort_type'] = sort_type
    context['is_authenticated'] = request.user.is_authenticated
    context['search_query'] = search_query  # Pass search query back to the template
    return render(request, 'properties/listing.html', context)

@csrf_exempt    
def deleteProperty(request, id):
    # Get the property object by id, or return a 404 if not found
    property_to_delete = get_object_or_404(Property, id=id)
    
    if request.method == "POST":
        property_to_delete.delete()
        return redirect('properties:listing') 



# WISHLIST ============================================

def add_to_wishlist(request, property_id):
        user = request.user
        property_to_add = Property.objects.get(id = property_id)
        wishlist,created = Wishlist.objects.get_or_create(account = user)
        wishlist.property.add(property_to_add)
        wishlist.save()
            

def remove_from_wishlist(request, property_id):
    user = request.user
    property_to_remove = get_object_or_404(Property, id=property_id)
    wishlist = Wishlist.objects.get(account=user)

    if property_to_remove in wishlist.property.all():
        wishlist.property.remove(property_to_remove)

    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required

def wishlists(request):
    # Ensure the user is a customer
    if not request.user.is_authenticated or request.user.role != 'customer':
        return redirect('restricted')

    user = request.user
    context = {}

    # Get the user's wishlist
    wishlist, created = Wishlist.objects.get_or_create(account=user)
    properties = wishlist.property.all()

    # Default sorting type and search query
    sort_type = "default"
    search_query = ""

    if request.method == "POST":
        # Search logic
        search_query = request.POST.get("searchQuery", "").strip()
        if search_query:
            if search_query.isdigit():  # If the search query is numeric
                min_value = int(search_query)
                max_value = min_value + (1000 if len(search_query) > 2 else 100) - 1
                properties = properties.filter(price__gte=min_value, price__lte=max_value)
            else:  # Search by name or address
                properties = properties.filter(
                    Q(name__icontains=search_query) | Q(address__icontains=search_query)
                )

        # Sorting logic
        if 'sortPriceHigher' in request.POST:
            properties = properties.order_by('-price')
            sort_type = "price_high"
        elif 'sortPriceLower' in request.POST:
            properties = properties.order_by('price')
            sort_type = "price_low"
        elif 'sortAlpha' in request.POST:
            properties = properties.order_by('name')
            sort_type = "alpha"
        elif 'sortRating' in request.POST:
            properties = properties.order_by('-rating')

        # Remove from wishlist
        if "remove_from_wishlist" in request.POST:
            property_id = request.POST.get("remove_from_wishlist")
            return remove_from_wishlist(request, property_id)

    # Pass data to the template
    context['properties'] = properties
    context['sort_type'] = sort_type  # Maintain the selected sorting option
    context['search_query'] = search_query  # Maintain the search input
    return render(request, "properties/wishlist.html", context)








#updateing the property: get the instance use it as a base form
    # property_instance = Property.objects.get(id=1)
    # form = PropertyForm(instance=property_instance)



#property lisint page
def hostProperties(request):
        properties = Property.objects.all()
        return render(request, 'properties/listing.html', {'properties': properties})




from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm
from .models import Property, Wishlist
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def create_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.host = request.user
            form.save()
            return redirect('landingpage')
    else:
        form = PropertyForm()

    return render(request, 'properties/create_property.html', {'form': form})
# if request.user.is_authenticated:
#     form.instance.host = request.user
# else:
#     form.add_error('host', 'You must be logged in to create a property.')

#property lisint page
def listing(request):
        properties = Property.objects.all()
        return render(request, 'properties/listing.html', {'properties': properties})

@csrf_exempt    
def deleteProperty(request, id):
    # Get the property object by id, or return a 404 if not found
    property_to_delete = get_object_or_404(Property, id=id)
    
    if request.method == "POST":
        property_to_delete.delete()
        return redirect('properties:listing') 

#wishlist================

def wishlist_view(request):
    # wishlists = Wishlist.objects.filter(user=request.user)
    wishlists = Wishlist.objects.all()
    return render(request, 'properties/wishlists.html', {'wishlists': wishlists})

def add_wishlist(request):
    if request.method == "POST":
        property_id = request.POST.get('property_id')  # Retrieve the property ID from POST
        property_obj = get_object_or_404(Property, id=property_id)
        account = request.user  # Using account instead of user

        # Check if the account already has a wishlist
        existing_wishlist = Wishlist.objects.filter(account=account).first()

        if existing_wishlist:
            # If a wishlist exists for the account, add the property to it
            if property_obj in existing_wishlist.property.all():
                message = "This property is already in your wishlist."
            else:
                existing_wishlist.property.add(property_obj)
                message = f"Property {property_obj.name} added to the wishlist."
        else:
            # If no wishlist exists, create a new one and add the property
            new_wishlist = Wishlist.objects.create(account=account)
            new_wishlist.property.add(property_obj)
            message = f"Property {property_obj.name} added to the wishlist."

        # Pass the message to the template
        return render(request, 'properties/listing.html', {'message': message})
    else:
        return HttpResponse("Invalid request method.", status=400)





#updateing the property: get the instance use it as a base form
    # property_instance = Property.objects.get(id=1)
    # form = PropertyForm(instance=property_instance)


#propertydetail==========================
def property_details(request, id):
    property = get_object_or_404(Property, id=id)  # Fetch the property with the given ID
    return render(request, 'properties/property.html', {'property': property})


#property lisint page
def hostProperties(request):
        properties = Property.objects.all()
        return render(request, 'properties/listing.html', {'properties': properties})

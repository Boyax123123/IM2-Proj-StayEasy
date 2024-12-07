from django.urls import path
from .views import booking_create, wishlists, host_property, create_property, listing, deleteProperty, add_to_wishlist,property_details, host_dashboard

app_name = 'properties'
urlpatterns = [
    path('create_property/', create_property, name='create_property'),
    path('edit/<int:pk>/', create_property, name='edit_property'),
    path('my_properties', host_property, name='my_properties'),
    path('listing/', listing, name='listing'),
    path('delete/<int:id>/', deleteProperty, name='delete_property'),

    path('property_details/<int:property_id>/', property_details, name = 'property_details'),
    path('host_dashboard/', host_dashboard, name = 'host_dashboard'),
   
    path('booking_create/', booking_create, name='booking_create'),

    path('wishlists', wishlists, name = 'wishlists'), 
   
]

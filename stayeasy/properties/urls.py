from django.urls import path
from .views import create_property, listing, deleteProperty, add_wishlist,wishlist_view,property_details

app_name = 'properties'
urlpatterns = [
    path('create_property/', create_property, name='create_property'),
    path('listing/', listing, name='listing'),
    path('delete/<int:id>/', deleteProperty, name='delete_property'),
    path('add_wishlist/', add_wishlist,name='add_wishlist'),
    path('wishlists/', wishlist_view, name = 'wishlists'),
    path('property_details/<int:id>/', property_details, name = 'property_details'),
]

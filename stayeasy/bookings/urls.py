# bookings/urls.py
from django.urls import path
from .views import my_bookings, cancel_booking

app_name = "bookings"

urlpatterns = [
    # Add your views and URLs here
    # For now, let's just add a placeholder view
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('cancel_booking/', cancel_booking, name='cancel_booking'),
]


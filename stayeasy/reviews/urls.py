from django.urls import path
from .views import add_review,property_reviews
app_name = "reviews"
urlpatterns = [
    path('add/<int:property_id>/<int:booking_id>/', add_review, name='add_review'),
    path('add/<int:property_id>/', property_reviews, name='property_reviews'),
]
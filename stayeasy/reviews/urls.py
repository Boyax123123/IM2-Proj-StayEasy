from django.urls import path
from .views import add_review
app_name = "reviews"
urlpatterns = [
    path('add_review', add_review, name='add_review'),
]
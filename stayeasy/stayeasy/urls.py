"""
URL configuration for stayeasy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import landingpage, restricted
from django.conf import settings
from django.conf.urls.static import static
from .views import set_test_date

app_name = 'stayeasy'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('', landingpage, name='landingpage'),
    path('restricted', restricted, name = "restricted"),
    path('property/', include('properties.urls')),
    path('reviews/', include('reviews.urls')),
    path('bookings/', include('bookings.urls')),
    path('set_test_date/', set_test_date, name='set_test_date'),  


]
if settings.DEBUG:  # Only add this when in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
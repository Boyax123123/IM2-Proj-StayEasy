from django.urls import path
from .views import deposit, signup_view, login_view, logout_view, test, profile

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name = "signup"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('test/', test, name = 'test'),
    path('profile/', profile, name = 'profile'),
    path('deposit/', deposit, name = "deposit")
]

from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    email = models.EmailField(max_length=150, null=False, unique=True)  
    password = models.CharField(max_length=255)#override para makita pass ig test
    first_name = models.CharField(max_length=50, null=False)  
    last_name = models.CharField(max_length=50, null=False)  
    phone_number = models.CharField(max_length=11, null=False)  
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    role = models.CharField(max_length=10, default="customer")  
    profile_picture = models.ImageField(default='images/iconProfileDefault.jpg', blank=True, upload_to='profile_pictures/' )  
    about_me = models.TextField(max_length=1000, blank=True) 

    
    USERNAME_FIELD = 'email'  

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  

    def __str__(self):
        return self.email 

from django.db import models
from accounts.models import Accounts


# Create your models here.


class Property(models.Model):
    host = models.ForeignKey(Accounts, on_delete=models.CASCADE, null = True, default = 5)
    name = models.CharField(max_length=255, null = False)
    description = models.TextField()
    address = models.CharField(max_length=255, null = False)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default = 0)
    image = models.ImageField(upload_to='uploads/', null = True, blank=True)



    def __str__(self):
        return self.name 




# class PropertyImage(models.Model):
#     property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='static/media/')

class Wishlist(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    property = models.ManyToManyField(Property)
    date_added = models.DateTimeField(auto_now_add=True)
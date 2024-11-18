# from django.db import models
# from accounts.models import Accounts
# from properties.models import Property

# # Create your models here.
# class Bookings(models.Model):
#     customer = models.ForeignKey(Accounts, on_delete = models.SET_NULL, null = True)
#     property = models.ForeignKey(Property, on_delete = models.SET_NULL, null = True)
#     checkin_date = models.DateField()
#     checkout_date = models.DateField()
#     total_cost  = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models
from accounts.models import Accounts
from properties.models import Property

class Bookings(models.Model):
    customer = models.ForeignKey(
        Accounts, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="bookings"
    )
    property = models.ForeignKey(
        Property, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="bookings"
    )
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
            ('completed', 'Completed')
        ],
        default='pending'
    )
    notes = models.TextField(blank=True, null=True) 

    class Meta:
        ordering = ['-booking_date']  
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Booking {self.id} - {self.customer} - {self.property}"

    def calculate_total_cost(self, daily_rate):
        """
        Utility method to calculate total cost based on daily rate and duration.
        """
        duration = (self.checkout_date - self.checkin_date).days
        self.total_cost = duration * daily_rate
        self.save()

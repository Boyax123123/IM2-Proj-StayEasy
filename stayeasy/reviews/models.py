from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from accounts.models import Accounts
from properties.models import Property
from bookings.models import Bookings

class Reviews(models.Model):
    customer = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, db_index=True)
    booking = models.ForeignKey(Bookings, on_delete=models.SET_NULL, null=True, db_index=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    review = models.TextField(max_length=1000, null=False, blank=False)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[
            MinValueValidator(1.0), 
            MaxValueValidator(5.0)
        ]
    )
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer} on {self.property.name[:10]} - Rating: {self.rating}"

    def clean(self):
        """Custom validation to ensure booking status is 'completed'."""
        if self.booking and self.booking.status != 'completed':
            raise ValidationError("Reviews can only be added for completed bookings.")

    def save(self, *args, **kwargs):
        """Override save to validate booking status."""
        self.full_clean()  # Ensure clean() is called before saving
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'reviews'

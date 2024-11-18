from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Accounts
from properties.models import Property

class Reviews(models.Model):
    customer = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, db_index=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    review = models.CharField(max_length=1000)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[
            MinValueValidator(1.0), 
            MaxValueValidator(5.0)
        ]
    )
    review_date = models.DateField(auto_now_add=True)
    helpful_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Review by {self.customer} on {self.property.name[:10]} - Rating: {self.rating}"
    
    class Meta:
        app_label = 'reviews'  # Add this if necessary

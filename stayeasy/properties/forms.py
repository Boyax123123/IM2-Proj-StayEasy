from django import forms
from .models import Property #Wishlist

class PropertyForm(forms.ModelForm):
        class Meta:
            model = Property
            fields = ['name', 'price', 'address', 'description','image']
            widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Property Name'}),
                'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
                'address': forms.TextInput(attrs={'placeholder': 'Property Address'}),
                'description': forms.Textarea(attrs={'placeholder': 'Details (e.g., amenities, host review)', 'rows': 4}),
                'image': forms.ClearableFileInput(attrs={'class': 'image-upload-input'}),
            }
            def clean_price(self):
                price = self.cleaned_data.get('price')
                if price <= 0:
                    raise forms.ValidationError('Price must be greater than zero.')
                return price

from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['property', 'title', 'review', 'rating']
        labels = {
            'property': 'Property',
            'title': 'Title (optional)',
            'review': 'Your Review',
            'rating': 'Rating (1.0 - 5.0)',
        }
        widgets = {
            'property': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Select Property'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a brief title for your review (optional)',
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here...',
                'rows': 4,
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a rating between 1.0 and 5.0',
                'min': 1.0,
                'max': 5.0,
                'step': 0.1,
            }),
        }

    # Optional: Custom Validation for Rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1.0 or rating > 5.0:
            raise forms.ValidationError('Rating must be between 1.0 and 5.0.')
        return rating

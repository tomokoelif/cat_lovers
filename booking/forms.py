from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'email', 'cat_name', 'breed', 'color',
            'gender', 'date'
        ]
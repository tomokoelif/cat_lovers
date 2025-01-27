from django import forms
from .models import Booking

TIME_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(8, 21)]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'cat_name', 'breed', 'color',
            'gender', 'date', 'time'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'style': 'color: black;'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=TIME_CHOICES),
        }
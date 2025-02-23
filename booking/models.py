from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Booking(models.Model):
    """ A model for making a booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=40)  # デフォルト値を削除
    email = models.EmailField()
    cat_name = models.CharField(max_length=20)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')])
    date = models.DateField(default=datetime.now, blank=True)
    time = models.TimeField(default='12:00:00')

    class Meta:
        """ Order bookings by date """
        ordering = ["-date"]
        unique_together = ['date']

    def __str__(self):
        return f"{self.cat_name} - {self.date} at {self.time}"
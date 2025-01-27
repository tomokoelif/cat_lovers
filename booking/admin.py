from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cat_name', 'breed', 'color', 'gender', 'date', 'time')
    
admin.site.register(Booking, BookingAdmin)
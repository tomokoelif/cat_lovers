from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
)


class BookingsPage(LoginRequiredMixin, ListView):
    """
    View booking page
    """
    model = Booking
    template_name = 'booking/booking_home_page.html'
    context_object_name = 'bookings'


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    Create a booking for registered users
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_home_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        selected_date = form.cleaned_data.get('date')
        current_datetime = timezone.now()

        # Check if date is in the past
        if selected_date < current_datetime.date():
            form.add_error('date', 'Great Scott! Do you have a time machine?')
            return self.form_invalid(form)

        # Check the number of active bookings for the current user
        active_bookings_count = Booking.objects.filter(
            user=self.request.user, date=form.instance.date).count()

        # Limit the maximum number of active bookings to 4
        if active_bookings_count >= 4:
            messages.error(
                self.request,
                "You have reached the maximum number of active bookings."
            )
            return redirect(self.success_url)

        messages.success(self.request, "Your booking has been created.")
        return super().form_valid(form)


class BookingEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit an already created booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_edit.html'
    success_url = reverse_lazy('booking_home_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete an existing booking
    """
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_home_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user
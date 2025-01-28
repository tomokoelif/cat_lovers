from django.test import TestCase
from booking.models import Booking
from django.core.exceptions import ValidationError

class BookingModelTest(TestCase):

    def test_booking_with_empty_name(self):
        """Test booking with an empty name"""
        booking = Booking(name='', email='test@test.com', cat_name='Whiskers', breed='Siamese', color='Brown', gender='Male', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_invalid_email(self):
        """Test booking with an invalid email"""
        booking = Booking(name='John Doe', email='invalid-email', cat_name='Whiskers', breed='Siamese', color='Brown', gender='Male', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_empty_cat_name(self):
        """Test booking with an empty cat name"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='', breed='Siamese', color='Brown', gender='Male', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_invalid_date(self):
        """Test booking with an invalid date"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='Whiskers', breed='Siamese', color='Brown', gender='Male', date='invalid-date', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_invalid_time(self):
        """Test booking with an invalid time"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='Whiskers', breed='Siamese', color='Brown', gender='Male', date='2025-01-01', time='invalid-time')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_empty_breed(self):
        """Test booking with an empty breed"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='Whiskers', breed='', color='Brown', gender='Male', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_empty_color(self):
        """Test booking with an empty color"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='Whiskers', breed='Siamese', color='', gender='Male', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_with_empty_gender(self):
        """Test booking with an empty gender"""
        booking = Booking(name='John Doe', email='test@test.com', cat_name='Whiskers', breed='Siamese', color='Brown', gender='', date='2025-01-01', time='10:00')
        with self.assertRaises(ValidationError):
            booking.full_clean()

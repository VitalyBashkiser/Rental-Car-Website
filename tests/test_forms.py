from django.test import TestCase
from car_rentals.forms import (
    BookingForm,
    CarSearchForm,
    ClientRegistrationForm,
)


class FormTests(TestCase):

    def test_booking_form(self):
        form_data = {"start_date": "2024-05-18", "end_date": "2024-05-20"}
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_search_form(self):
        form_data = {"query": "Toyota"}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_client_registration_form(self):
        form_data = {
            "username": "testuser",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        form = ClientRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

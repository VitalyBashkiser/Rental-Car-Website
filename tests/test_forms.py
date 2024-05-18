from django.test import TestCase
from car_rentals.forms import BookingForm, CarSearchForm


class BookingFormTests(TestCase):

    def test_valid_booking_form(self):
        form_data = {"start_date": "2024-05-18", "end_date": "2024-05-20"}
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form(self):
        form_data = {"start_date": "2024-05-20", "end_date": "2024-05-18"}
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())


class CarSearchFormTests(TestCase):

    def test_valid_car_search_form(self):
        form_data = {"query": "Toyota"}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_car_search_form(self):
        form_data = {"query": ""}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

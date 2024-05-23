from django.test import TestCase, Client
from django.urls import reverse
from car_rentals.models import Car


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.car = Car.objects.create(
            make="Toyota", model="Camry", year=2020, price_per_day=50.00
        )

    def test_car_list_view(self):
        url = reverse("car_rentals:car-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_car_detail_view(self):
        url = reverse("car_rentals:car-detail", args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_book_car_view(self):
        url = reverse("car_rentals:book-car", args=[self.car.id])
        response = self.client.post(
            url, {"start_date": "2024-05-18", "end_date": "2024-05-20"}
        )
        self.assertEqual(response.status_code, 302)

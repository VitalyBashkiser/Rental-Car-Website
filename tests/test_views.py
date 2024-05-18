from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from car_rentals.models import Car, Booking


class CarTests(TestCase):

    def setUp(self):
        self.car = Car.objects.create(
            make="Toyota", model="Camry", year=2020, price_per_day=50.00
        )

    def test_car_list_view(self):
        response = self.client.get(reverse("car_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.make)
        self.assertTemplateUsed(response, "car_rentals/car_list.html")

    def test_car_detail_view(self):
        response = self.client.get(reverse("car_detail", args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.model)
        self.assertTemplateUsed(response, "car_rentals/car_detail.html")

    def test_booking_creation(self):
        user = User.objects.create_user(username="user1", password="password")
        self.client.login(username="user1", password="password")
        response = self.client.post(
            reverse("book_car", args=[self.car.id]),
            {
                "start_date": "2024-05-18",
                "end_date": "2024-05-20",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.user, user)
        self.assertEqual(booking.car, self.car)
        self.assertEqual(booking.total_cost, 100.00)

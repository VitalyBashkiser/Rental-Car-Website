from django.test import TestCase
from django.urls import reverse
from car_rentals.models import Car, Booking, Transaction, Client


class AdminViewTests(TestCase):
    def setUp(self):
        self.admin = Client.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
        )

    def test_admin_car_list_view(self):
        self.client.force_login(self.admin)
        url = reverse("admin:car_rentals_car_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/change_list.html")

    def test_admin_booking_list_view(self):
        self.client.force_login(self.admin)
        url = reverse("admin:car_rentals_booking_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/change_list.html")

    def test_admin_transaction_list_view(self):
        self.client.force_login(self.admin)
        url = reverse("admin:car_rentals_transaction_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/change_list.html")

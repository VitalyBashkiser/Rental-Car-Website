from django.test import TestCase
from car_rentals.models import Client, Car, Booking, Transaction


class ModelTests(TestCase):

    def test_client_model(self):
        client = Client.objects.create_user(
            username="testuser",
            password="password",
            email="test@example.com",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(client.__str__(), "testuser")

    def test_car_model(self):
        car = Car.objects.create(
            make="Toyota", model="Camry", year=2020, price_per_day=50.00
        )
        self.assertEqual(car.__str__(), "Toyota Camry (2020)")

    def test_booking_model(self):
        client = Client.objects.create_user(
            username="testuser", password="password", email="test@example.com"
        )
        car = Car.objects.create(
            make="Toyota", model="Camry", year=2020, price_per_day=50.00
        )
        booking = Booking.objects.create(
            car=car,
            user=client,
            start_date="2024-05-18",
            end_date="2024-05-20",
            total_cost=100.00,
        )
        self.assertEqual(
            booking.__str__(),
            f"Booking {booking.id} - {booking.car} by {booking.user}",
        )

    def test_transaction_model(self):
        client = Client.objects.create_user(
            username="testuser", password="password", email="test@example.com"
        )
        car = Car.objects.create(
            make="Toyota", model="Camry", year=2020, price_per_day=50.00
        )
        booking = Booking.objects.create(
            car=car,
            user=client,
            start_date="2024-05-18",
            end_date="2024-05-20",
            total_cost=100.00,
        )
        transaction = Transaction.objects.create(
            booking=booking, amount=100.00, payment_method="Credit Card"
        )
        self.assertEqual(
            transaction.__str__(),
            f"Transaction {transaction.id} - {transaction.booking}",
        )

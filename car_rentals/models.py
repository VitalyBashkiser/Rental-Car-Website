from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, validators=[EmailValidator()])

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "user"

    def __str__(self):
        return self.username


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Booking(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name="bookings"
    )
    user = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} - {self.car} by {self.user}"


class Transaction(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Transaction {self.id} - {self.booking}"

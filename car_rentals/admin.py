from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from car_rentals.models import Car, Booking, Transaction, Client


@admin.register(Client)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "year", "price_per_day")
    search_fields = ("make", "model")
    list_filter = ("year",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("car", "user", "start_date", "end_date", "total_cost")
    search_fields = ("car__make", "car__model", "user__username")
    list_filter = ("start_date", "end_date")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("booking", "transaction_date", "amount", "payment_method")
    search_fields = (
        "booking__car__make",
        "booking__car__model",
        "booking__user__username",
    )
    list_filter = ("transaction_date",)

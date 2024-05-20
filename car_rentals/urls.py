from django.urls import path

from car_rentals.views import (
    CarDetailView,
    BookCarView,
    MyBookingsView,
    CarListView,
    ClientView,
    RegisterView,
)

urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("book/<int:car_id>/", BookCarView.as_view(), name="book-car"),
    path("my-bookings/", MyBookingsView.as_view(), name="my-bookings"),
    path('client/', ClientView.as_view(), name='client'),
    path('register/', RegisterView.as_view(), name='register'),
]

app_name = "car_rentals"

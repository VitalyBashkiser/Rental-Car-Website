from django.urls import path

from Car_sharing.car_rentals import views

urlpatterns = [
    path("", views.car_list, name="car_list"),
    path("car/<int:car_id>/", views.car_detail, name="car_detail"),
    path("car/<int:car_id>/book/", views.book_car, name="book_car"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
]

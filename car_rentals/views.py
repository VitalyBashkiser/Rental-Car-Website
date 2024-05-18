from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from car_rentals.models import Car, Booking
from car_rentals.forms import BookingForm


def car_list(request):
    query = request.GET.get("q")
    if query:
        cars = Car.objects.filter(make__icontains=query) | Car.objects.filter(
            model__icontains=query
        )
    else:
        cars = Car.objects.all()
    return render(
        request, "car_rentals/car_list.html", {"cars": cars, "query": query}
    )


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, "car_rentals/car_detail.html", {"car": car})


@login_required
def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.user = request.user
            booking.total_cost = (
                booking.end_date - booking.start_date
            ).days * car.price_per_day
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect("car_detail", car_id=car.id)
    else:
        form = BookingForm()
    return render(
        request, "car_rentals/book_car.html", {"form": form, "car": car}
    )


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(
        request, "car_rentals/my_bookings.html", {"bookings": bookings}
    )

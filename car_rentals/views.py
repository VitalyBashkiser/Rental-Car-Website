from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from car_rentals.models import Car, Booking, Client
from car_rentals.forms import BookingForm


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "car_rentals/car_list.html"
    context_object_name = "cars"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Car.objects.filter(
                make__icontains=query
            ) | Car.objects.filter(model__icontains=query)
        return Car.objects.all()


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    template_name = "car_rentals/car_detail.html"
    context_object_name = "car"


class BookCarView(LoginRequiredMixin, generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "car_rentals/book_car.html"

    def form_valid(self, form):
        car_id = self.kwargs["car_id"]
        car = get_object_or_404(Car, id=car_id)
        booking = form.save(commit=False)
        booking.car = car
        booking.user = self.request.user
        booking.total_cost = (
            booking.end_date - booking.start_date
        ).days * car.price_per_day
        booking.save()
        messages.success(self.request, "Booking successful!")
        return redirect("car_rentals:car-detail", pk=car.id)


class MyBookingsView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = "car_rentals/my_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class ClientView(LoginRequiredMixin, generic.ListView):
    template_name = "car_rentals/client.html"
    model = Client
    context_object_name = "clients"


class RegisterView(generic.View):
    def get(self, request):
        form = ClientRegistrationForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "registration/register.html", {"form": form})

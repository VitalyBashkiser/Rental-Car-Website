# RentalCarService

Rental Car Service is a web-based car rental application that allows users to book cars online.
The application provides functionality for managing users, cars, reservations and transactions.

```shell
git clone https://github.com/VitalyBashkiser/Rental-Car-Website.git
cd Rental-Car-Website

python -m venv venv
source venv/bin/activate # on macOS/Linux
venv\Scripts\activate # on Windows
Install dependencies:

pip install -r requirements.txt

python manage.py migrate
Create a superuser to access the admin panel:

python manage.py createsuperuser
Start the development server:

python manage.py runserver
```

## Features

* Registration and Authentication: Users can register and login.
* View Cars: Users can view a list of available cars.
* Car booking: Registered users can book cars by specifying rental dates.
* View Bookings: We can view their current bookings.

## Demo

![Wedsite Interface](Demo.png)

## Test user for test my website:

* login: user
* password: user12345
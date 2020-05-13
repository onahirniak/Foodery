## Overview
A service Foodery.MobileApi responsible for communicating between mobile application and other services.
Basicaly the service is [Backend-For-Frontend](https://samnewman.io/patterns/architectural/bff/) for mobile app.

## Working with solution:
You have to install python3 >= 3.7.4 and pip >= 20.1

### Run host:
Run host: python manage.py run

### Working with migrations:
Migrations init: 
python manage.py db init

Add migrations:
python manage.py db migrate --message 'initial database migration'

Migrate database:
python manage.py db upgrade

### Run tests:
python manage.py test

## Working with solutions inside Docker:

### Build image:
docker build --tag foodery-mobileapi:latest .

### Run host:
docker run -p 5000:5000 foodery-mobileapi api

### Migrate database:
docker run -p 5000:5000 --network host foodery-mobileapi migrate

### Run tests:
docker run -p 5000:5000 --network host foodery-mobileapi test

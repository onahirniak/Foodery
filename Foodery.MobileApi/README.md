## Overview
A service Foodery.MobileApi responsible for communicating between mobile application and other services.
Basicaly the service is [Backend-For-Frontend](https://samnewman.io/patterns/architectural/bff/) for mobile app.

## Working with solution:
You have to install python3 >= 3.7.4 and pip >= 20.1

### Run host:
Run host: 
```bash 
python manage.py run
```

### Working with migrations:
Migrations init: 
```bash 
python manage.py db init
```
Add migrations:
```bash 
python manage.py db migrate --message 'initial database migration'
```
Migrate database:
```bash 
python manage.py db upgrade
```
### Run tests:
```bash 
python manage.py test
```
## Working with solutions inside Docker:

### Build image:
```bash 
docker build --tag foodery-mobileapi:latest .
```
### Run host:
```bash 
docker run -p 5000:5000 foodery-mobileapi api
```
### Migrate database:
```bash 
docker run -p 5000:5000 --network host foodery-mobileapi migrate
```
### Run tests:
```bash 
docker run -p 5000:5000 --network host foodery-mobileapi test
```

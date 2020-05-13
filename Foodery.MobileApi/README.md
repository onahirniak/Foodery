## Working with solution:
Run host: python manage.py run

### Working with migrations:
Migrations init: 
python manage.py db init

Add migrations:
python manage.py db migrate --message 'initial database migration'

Migrate database:
python manage.py db upgrade

### Testing:
python manage.py test

## Running inside Docker:

### Build image:
docker build --tag foodery-mobileapi:latest .

### Host:
docker run -p 5000:5000 foodery-mobileapi api

### Migrate database:
docker run -p 5000:5000 --network host foodery-mobileapi migrate

### Testing:
docker run -p 5000:5000 --network host foodery-mobileapi test

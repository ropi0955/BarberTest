#!/bin/bash

python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

gunicorn --bind :8000 --workers 2 BarberShopTest.wsgi
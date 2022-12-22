#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=abc@abc.ab
export DJANGO_SUPERUSER_PASSWORD=passwordDePrueba

python manage.py createsuperuser --no-input

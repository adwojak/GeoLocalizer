#!/usr/bin/env bash

virtualenv -p python3.8 venv
source "./venv/bin/activate"
pip install -r requirements
python manage.py makemigrations geolocalizer
python manage.py migrate

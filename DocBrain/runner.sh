#!/usr/bin/env sh

# Getting static files for Admin panel hosting!
set -e

# Getting static files for Admin panel hosting!

python manage.py collectstatic --noinput

cp -r /app/staticfiles /static/

#app startup
gunicorn tnibroproject.wsgi:application --workers 4 --bind 0.0.0.0:8000 --timeout 300
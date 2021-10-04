#!/bin/sh

echo "Waiting for database ..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "Database started"

alembic upgrade head
uwsgi --http-socket 0.0.0.0:5000 --wsgi-file wsgi.py --callable application --processes 4 --threads 2

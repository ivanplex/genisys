#!/bin/bash

# python manage.py migrate

# python manage.py collectstatic

# Start the server
gunicorn genisys.wsgi -w 2 -b :8080
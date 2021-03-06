#!/bin/bash
python manage.py migrate                  # Apply database migrations
# python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
#touch /srv/logs/gunicorn.log
#touch /srv/logs/access.log
#tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
#echo Starting Gunicorn.
#exec gunicorn genisys.wsgi:application \
#    --name modular_assembly_API \
#    --bind 0.0.0.0:8080 \
#    --workers 3 \
##    --log-level=info \
##    --log-file=/srv/logs/gunicorn.log \
##    --access-logfile=/srv/logs/access.log \
#    "$@"

# FOR DEVELOPMENT ONLY!
python manage.py runserver 0.0.0.0:8080 --settings=modular_assembly.settings.settings_prod
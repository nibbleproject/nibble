#!/bin/bash
#
# Usage: python_test.sh

export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'
export DATABASE_URL='sqlite:///ci.db'
export DJANGO_SETTINGS_MODULE='minicomi.settings.production'

pep8 .
coverage run --source='.' manage.py test

# Set things up
python manage.py migrate
python manage.py minicomi_setup

# Get that server going
python manage.py runserver 127.0.0.1:5000 --noreload > server.log 2>&1 &
MINICOMI_PID=$!

behave

# Get that server not going
kill -TERM $MINICOMI_PID
rm ci.db

if [ -n "$COVERALLS_REPO_TOKEN" ]; then
    coveralls
fi

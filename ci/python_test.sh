#!/bin/bash
#
# Usage: python_test.sh

set -e

export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'
export DATABASE_URL='sqlite:///ci.db'
export DJANGO_SETTINGS_MODULE='minicomi.settings.production'

pep8 .
coverage run --source='.' manage.py test

if [ -n "$COVERALLS_REPO_TOKEN" ]; then
    coveralls
fi

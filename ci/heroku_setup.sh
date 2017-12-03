#!/bin/bash
#
# Usage: heroku_setup.sh CURRENT_COMMIT APP_NAME HEROKU_AUTH_TOKEN

HEROKU_AUTH_TOKEN="$3"
HEROKU_APP_NAME="$2"

export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'

pip install -r requirements-test.txt

# Create a Heroku app
happy up \
    --auth-token $HEROKU_AUTH_TOKEN \
    --env SUPERUSER_NAME=$SUPERUSER_NAME \
    --env SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
    --env SUPERUSER_EMAIL=$SUPERUSER_EMAIL \
    --tarball-url https://github.com/grampajoe/minicomi/tarball/$1/ \
    $HEROKU_APP_NAME

#!/bin/bash
#
# Usage: test-heroku.sh APP_NAME HEROKU_AUTH_TOKEN

HEROKU_AUTH_TOKEN="$2"
HEROKU_APP_NAME="$1"
export MINICOMI_ALT_DOMAIN="$HEROKU_APP_NAME.joefriedl.net"
export MINICOMI_BASE_URL="https://$HEROKU_APP_NAME.herokuapp.com"

export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'

# Run integration tests
behave

# Destroy the Heroku app
happy down \
    --auth-token $HEROKU_AUTH_TOKEN \
    --force \
    $HEROKU_APP_NAME

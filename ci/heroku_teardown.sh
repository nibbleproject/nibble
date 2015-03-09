#!/bin/bash
#
# Usage: heroku_teardown.sh APP_NAME HEROKU_AUTH_TOKEN

HEROKU_APP_NAME="$1"
HEROKU_AUTH_TOKEN="$2"

# Destroy the Heroku app
happy down \
    --auth-token $HEROKU_AUTH_TOKEN \
    --force \
    $HEROKU_APP_NAME

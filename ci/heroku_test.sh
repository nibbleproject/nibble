#!/bin/bash
#
# Usage: test-heroku.sh CURRENT_COMMIT HEROKU_AUTH_TOKEN

HEROKU_AUTH_TOKEN="$2"
HEROKU_APP_NAME="ci-minicomi-`date '+%s'`"
export MINICOMI_ALT_DOMAIN="$HEROKU_APP_NAME.joefriedl.net"
export MINICOMI_BASE_URL="https://$HEROKU_APP_NAME.herokuapp.com"

export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'

# Create a Heroku app
happy up \
    --auth-token $HEROKU_AUTH_TOKEN \
    --env SUPERUSER_NAME=$SUPERUSER_NAME \
    --env SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
    --env SUPERUSER_EMAIL=$SUPERUSER_EMAIL \
    --tarball-url https://github.com/grampajoe/minicomi/tarball/$1/ \
    $HEROKU_APP_NAME

# Add a custom domain
curl -n -X POST https://api.heroku.com/apps/$HEROKU_APP_NAME/domains \
    -H "Authorization: Bearer $HEROKU_AUTH_TOKEN" \
    -H "Accept: application/vnd.heroku+json; version=3" \
    -H "Content-Type: application/json" \
    -d "{\"hostname\": \"$MINICOMI_ALT_DOMAIN\"}";

# Run integration tests
behave

# Destroy the Heroku app
happy down \
    --auth-token $HEROKU_AUTH_TOKEN \
    --force \
    $HEROKU_APP_NAME

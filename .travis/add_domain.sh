#!/bin/bash

curl -n -X POST https://api.heroku.com/apps/$HEROKU_APP_NAME/domains \
    -H "Authorization: Bearer $HEROKU_AUTH_TOKEN" \
    -H "Accept: application/vnd.heroku+json; version=3" \
    -H "Content-Type: application/json" \
    -d "{\"hostname\": \"$1\"}";

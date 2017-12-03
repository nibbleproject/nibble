#!/bin/bash
#
# Usage: heroku_test.sh APP_NAME

set -e

HEROKU_APP_NAME="$1"

# Run integration tests
make smoke REMOTE_URL="https://$HEROKU_APP_NAME.herokuapp.com"

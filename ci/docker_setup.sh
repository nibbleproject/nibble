#!/bin/bash
#
# Usage: docker_setup.sh

set -e

pip install -r requirements_test.txt

docker build -t minicomi .

DOCKER_IP="$1"
export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'

if [ -z "$DOCKER_IP" ]; then
    DOCKER_IP='127.0.0.1'
fi

# Start the database
docker run -d --name minicomi-postgres postgres

# Start the app
docker run -d --name minicomi \
    --link minicomi-postgres:postgres \
    -p 5000:5000 \
    -e MINICOMI_DATABASE_PASSWORD=butt \
    -e SUPERUSER_NAME=$SUPERUSER_NAME \
    -e SUPERUSER_PASSWORD=$SUPERUSER_PASSWORD \
    -e SUPERUSER_EMAIL=$SUPERUSER_EMAIL \
    minicomi

while ! curl -sI $DOCKER_IP:5000; do
    echo 'Waiting for the app to start...'
    sleep 3
done

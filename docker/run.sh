#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=minicomi.settings.production
export PORT=5000

if [ -n "$POSTGRES_PORT_5432_TCP_ADDR" ];
then
    echo 'We got postgres!!!!'

    echo 'Creating database...'
    export PGPASSWORD="$POSTGRES_PASSWORD"
    psql \
        -h "$POSTGRES_PORT_5432_TCP_ADDR" \
        -p "$POSTGRES_PORT_5432_TCP_PORT" \
        -U "$POSTGRES_USER" \
        < docker/database_up.psql

    export DATABASE_URL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_PORT_5432_TCP_ADDR:$POSTGRES_PORT_5432_TCP_PORT/minicomi"
elif [ -n "$DATABASE_URL" ];
then
    echo "There's a database url already...???"
else
    echo 'No database ¯\_(ツ)_/¯'
    exit 1
fi

if [ "$1" = 'start' ];
then
    python3 manage.py migrate

    exec gunicorn \
        --workers=2 \
        --worker-class=gaiohttp \
        --access-logfile - \
        --bind=0.0.0.0:$PORT \
        minicomi.wsgi
else
    exec "$@"
fi

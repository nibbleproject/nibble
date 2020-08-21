#!/bin/bash

if [ "$1" = 'start' ];
then
	if [ -n "$DATABASE_URL" ]; then

		echo "Found a database URL, skipping setup."

	elif [ -n "$POSTGRES_PORT_5432_TCP_ADDR" ]; then

		echo 'We got postgres!!!!'

		if [ -z "$DATABASE_USER" ]; then
			echo 'No application database user defined. Stopping.'
			exit 1
		fi

		if [ -z "$DATABASE_PASSWORD" ]; then
			echo 'No application database password defined. Stopping.'
			exit 1
		fi

		: ${POSTGRES_USER:=$POSTGRES_ENV_POSTGRES_USER}
		: ${POSTGRES_PASSWORD:=$POSTGRES_ENV_POSTGRES_PASSWORD}

		if [ -z "$POSTGRES_USER" ]; then
			echo 'No Postgres root username defined. Assuming "postgres".'
			export POSTGRES_USER=postgres
		fi

		if [ -z "$POSTGRES_PASSWORD" ]; then
			echo 'No Postgres root user password defined. Assuming none.'
		fi

		export PGUSER="$POSTGRES_USER"
		export PGPASSWORD="$POSTGRES_PASSWORD"
		export PGHOST="$POSTGRES_PORT_5432_TCP_ADDR"
		export PGPORT="$POSTGRES_PORT_5432_TCP_PORT"

		if [ "$1" = 'start' ]; then
			while true; do
				echo 'Checking for postgres connectivity...'
				psql -c 'select 1;' 2>&1 > /dev/null && break
				sleep 1
			done

			echo 'Creating user...'

			createuser -e \
				$DATABASE_USER

			echo 'Creating database...'
			createdb -e \
				-E UTF8 \
				$DATABASE_NAME

			echo 'Setting password...'
			psql \
				-c "ALTER USER $DATABASE_USER PASSWORD '$DATABASE_PASSWORD';"

			echo 'Setting permissions...'
			psql -e \
				-c "GRANT ALL ON DATABASE $DATABASE_NAME TO $DATABASE_USER;"

			echo 'Database setup complete!'
		fi

		export DATABASE_URL="postgres://$DATABASE_USER:$DATABASE_PASSWORD@$POSTGRES_PORT_5432_TCP_ADDR:$POSTGRES_PORT_5432_TCP_PORT/$DATABASE_NAME"

	else
		echo 'No database defined, stopping. ¯\_(ツ)_/¯'
		exit 1
	fi

    python manage.py migrate

    if [ -n "$SUPERUSER_NAME" ]; then
        python manage.py nibble_setup
    fi

    exec gunicorn \
        --workers=2 \
        --worker-class=gthread \
        --access-logfile - \
        --bind=0.0.0.0:$PORT \
        nibble.wsgi
else
    exec "$@"
fi

#!/bin/bash

if [ "$1" = 'start' ];
then
	for i in $(seq 1 30); do
		python manage.py migrate
		if [[ "$?" -ne "0" ]]; then
			echo "Error setting up database, retrying..."
			sleep 1
		else
			break
		fi
	done

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

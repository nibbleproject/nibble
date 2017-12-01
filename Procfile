web: gunicorn --workers=2 --worker-class=aiohttp.worker.GunicornWebWorker --bind=0.0.0.0:$PORT minicomi.wsgi --access-logfile -

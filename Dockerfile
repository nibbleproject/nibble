FROM python:3.6.3

ENV DJANGO_SETTINGS_MODULE=nibble.settings.production
ENV DATABASE_NAME=nibble
ENV DATABASE_USER=test

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app/

RUN apt-get update && apt-get -y install postgresql-client && pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 5000

ENTRYPOINT ["docker/run.sh"]
CMD ["start"]

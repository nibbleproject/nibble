FROM ubuntu:14.04

COPY . /opt/minicomi
WORKDIR /opt/minicomi

ENV DJANGO_SETTINGS_MODULE=minicomi.settings.production
ENV MINICOMI_DATABASE_NAME=minicomi
ENV MINICOMI_DATABASE_USER=minicomi

RUN docker/install.sh

EXPOSE 5000

ENTRYPOINT ["docker/run.sh"]
CMD ["start"]

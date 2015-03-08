FROM ubuntu:14.04

COPY ./requirements.txt /opt/minicomi/requirements.txt
COPY ./docker/install.sh /opt/minicomi/docker/install.sh
WORKDIR /opt/minicomi

ENV DJANGO_SETTINGS_MODULE=minicomi.settings.production
ENV MINICOMI_DATABASE_NAME=minicomi
ENV MINICOMI_DATABASE_USER=minicomi

RUN docker/install.sh

COPY . /opt/minicomi

RUN docker/post-install.sh

EXPOSE 5000

ENTRYPOINT ["docker/run.sh"]
CMD ["start"]

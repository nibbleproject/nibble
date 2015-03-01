FROM ubuntu:14.04

COPY . /opt/minicomi
WORKDIR /opt/minicomi

RUN docker/install.sh

EXPOSE 5000

ENTRYPOINT ["docker/run.sh"]
CMD ["start"]

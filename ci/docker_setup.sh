#!/bin/bash
#
# Usage: docker_setup.sh

pip install -r requirements_test.txt

docker build -t minicomi .
docker pull postgres

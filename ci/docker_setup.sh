#!/bin/bash
#
# Usage: docker_setup.sh

pip install -r requirements_test.txt

docker pull postgres
docker build -t minicomi .

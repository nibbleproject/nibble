#!/bin/bash
#
# Usage: setup.sh

pip install -r requirements_test.txt
pip install -r requirements.txt

docker build -t minicomi .
docker pull postgres

#!/bin/bash
#
# Usage: python_test.sh

pep8 .
coverage run --source='.' manage.py test

coveralls

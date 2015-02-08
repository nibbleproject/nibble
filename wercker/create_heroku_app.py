"""
Creates a Heroku app with the app.json manifest.

Usage: create_heroku_app.py <git_ref> <app_name>
"""
import logging
import sys
import json
from time import sleep

import requests

from heroku import api_request


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def create_build(git_ref, app_name):
    """Creates a heroku app build, returning the build ID."""
    data = {
        'source_blob': {
            'url': 'https://github.com/grampajoe/minicomi/tarball/%s' % git_ref,
        },
        'app': {
            'name': app_name
        }
    }

    response = api_request('POST', 'app-setups', data=json.dumps(data))

    return response['id']


def check_build_status(build_id):
    """Checks the status of a build.

    Returns True for success, False for pending, and raises an exception for
    failure.
    """
    response = api_request('GET', 'app-setups/%s' % build_id)

    status = response['status']

    if status == 'failed':
        raise Exception('Ah jeez')

    return bool(status == 'succeeded')


if __name__ == '__main__':
    git_ref = sys.argv[1]
    app_name = sys.argv[2]

    build_id = create_build(git_ref, app_name)

    log.info('Created app %s. Building...' % app_name)

    while True:
        sleep(3)
        try:
            result = check_build_status(build_id)
        except Exception as e:
            log.exception('It broked')
            sys.exit(1)

        if result:
            log.info('Build succeeded!')
            sys.exit(0)

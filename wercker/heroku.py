"""
Heroku helper methods.
"""
import os

import requests


def _get_headers():
    """Returns a dict of headers for API requests."""
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.heroku+json; version=3',
        'Authorization': 'Bearer %s' % os.environ['HEROKU_AUTH_TOKEN'],
    }


def api_request(method, path, headers=None, data=None):
    """Makes a Heroku API request."""
    url = 'https://api.heroku.com/%s' % path
    headers = headers or {}
    headers.update(_get_headers())

    response = requests.request(method, url, data=data, headers=headers)

    if not response.ok:
        raise Exception('API request failed: %s' % response.content)

    return response.json()

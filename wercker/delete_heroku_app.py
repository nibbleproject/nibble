"""
Deletes a Heroku app by app ID.

Usage: delete_heroku_app.py <app_id>
"""
import logging
import sys

import requests

from heroku import api_request


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def delete_heroku_app(app_id):
    """Deletes the Heroku app given by app_id."""
    api_request('DELETE', 'apps/%s' % app_id)


if __name__ == '__main__':
    app_id = sys.argv[1]

    delete_heroku_app(app_id)

    log.info('App %s deleted.' % app_id)
    sys.exit(0)

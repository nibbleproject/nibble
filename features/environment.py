import os
import pdb

from selenium import webdriver
from splinter import Browser


def before_all(context):
    def get_browser():
        """Only create a browser if we need it."""
        try:
            browser = context.browser
        except AttributeError:
            options = webdriver.ChromeOptions()

            # Disable the sandbox and run in headless mode when running in CI
            if os.environ.get('CI'):
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')

            browser = context.browser = Browser('chrome', options=options)

        return browser
    context.get_browser = get_browser

    # Remote URL for smoke testing
    context.remote_url = os.environ.get('REMOTE_URL', 'http://localhost:5000')


def _debug():
    """Returns a bool indicating whether debug mode is on."""
    return os.environ.get('BEHAVE_PDB')


def after_step(context, step):
    if _debug() and step.status == 'failed':
        pdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    try:
        context.browser.quit()
        del context.browser
    except AttributeError:
        pass

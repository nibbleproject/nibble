import os
import pdb

from splinter import Browser


def before_all(context):
    def get_browser():
        """Only create a browser if we need it."""
        try:
            browser = context.browser
        except AttributeError:
            browser = context.browser = Browser('firefox')
        return browser

    context.remote_url = os.environ.get('REMOTE_URL', 'http://localhost:5000')
    context.get_browser = get_browser


def _debug(context):
    """Returns a bool indicating whether debug mode is on."""
    return context.config.userdata.getbool('BEHAVE_PDB')


def after_step(context, step):
    if _debug(context) and step.status == 'failed':
        pdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    try:
        context.browser.quit()
        del context.browser
    except AttributeError:
        pass

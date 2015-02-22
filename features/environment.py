import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def _get_driver():
    """Returns a Sauce Labs driver if available, otherwise Firefox."""
    username = os.environ.get('SAUCE_LABS_USERNAME')
    key = os.environ.get('SAUCE_LABS_KEY')

    if username and key:
        url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'
        driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor=url % (username, key),
        )
    else:
        driver = webdriver.Firefox()

    return driver


def before_all(context):
    context.base_url = os.environ.get(
        'MINICOMI_BASE_URL',
        'http://localhost:5000',
    )
    context.browser = _get_driver()
    context.browser.implicitly_wait(3)


def after_all(context):
    context.browser.quit()

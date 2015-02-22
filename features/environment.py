import os

from selenium import webdriver


def before_all(context):
    context.base_url = os.environ.get(
        'MINICOMI_BASE_URL',
        'http://localhost:5000',
    )
    context.admin_url = context.base_url + '/admin'
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(3)


def after_all(context):
    context.browser.quit()

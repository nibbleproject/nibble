import os

from behave import given, when, then


USERNAME = os.environ.get('SUPERUSER_NAME', 'grampajoe')
PASSWORD = os.environ.get('SUPERUSER_PASSWORD', 'butt')


@when(u'I go to the admin page')
def step_impl(context):
    context.browser.get(context.admin_url)


@when(u'I enter my username and password')
def step_impl(context):
    browser = context.browser
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    password.submit()


@then(u'I should be logged in as an admin')
def step_impl(context):
    browser = context.browser
    page_text = browser.find_element_by_tag_name('body').text

    assert 'Django administration' in page_text
    assert 'Welcome, %s.' % USERNAME in page_text

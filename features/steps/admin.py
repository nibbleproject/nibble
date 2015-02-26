import os

from behave import given, when, then


USERNAME = os.environ.get('SUPERUSER_NAME', 'grampajoe')
PASSWORD = os.environ.get('SUPERUSER_PASSWORD', 'butt')
EMAIL = os.environ.get('SUPERUSER_EMAIL', 'butt@joefriedl.net')


@when(u'I go to the admin page')
def step_impl(context):
    context.get_browser().get(context.base_url + '/admin')


@when(u'I enter my username and password')
def step_impl(context):
    browser = context.get_browser()
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    password.submit()


@when(u'I go to my user page')
def step_impl(context):
    browser = context.get_browser()
    section_link = browser.find_element_by_link_text('Users')
    section_link.click()
    page_link = browser.find_element_by_link_text(USERNAME)
    page_link.click()


@then(u'I should be logged in as an admin')
def step_impl(context):
    browser = context.get_browser()
    page_text = browser.find_element_by_tag_name('body').text

    assert 'Django administration' in page_text
    assert 'Welcome, %s.' % USERNAME in page_text


@then(u'I should see the email address I chose')
def step_impl(context):
    browser = context.get_browser()
    email_field = browser.find_element_by_name('email')

    assert EMAIL in email_field.get_attribute('value')

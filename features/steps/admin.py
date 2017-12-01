from behave import when, then, given

from django.contrib.auth.models import User


ADMIN_USERNAME = 'test'
ADMIN_PASSWORD = 'test'
ADMIN_EMAIL = 'test@example.com'


@given(u'an admin user exists')
def create_user(context):
    context.admin = User.objects.create_user(
        username=ADMIN_USERNAME,
        password=ADMIN_PASSWORD,
        email=ADMIN_EMAIL,
        is_staff=True,
        is_superuser=True,
    )


@when(u'I go to the admin page')
def step_impl(context):
    context.get_browser().visit(context.base_url + '/admin')


@when(u'I enter my username and password')
def step_impl(context):
    browser = context.get_browser()

    browser.find_by_name('username').fill(ADMIN_USERNAME)
    browser.find_by_name('password').fill(ADMIN_PASSWORD)
    browser.find_by_value('Log in').first.click()


@when(u'I go to my user page')
def step_impl(context):
    browser = context.get_browser()

    browser.click_link_by_text('Users')
    browser.click_link_by_text(ADMIN_USERNAME)


@then(u'I should be logged in as an admin')
def step_impl(context):
    browser = context.get_browser()

    page_text = browser.find_by_tag('body').first.text

    assert browser.is_text_present('Django administration')
    assert browser.is_text_present(
        'Welcome, {}.'.format(ADMIN_USERNAME).upper()
    )


@then(u'I should see the email address I chose')
def step_impl(context):
    browser = context.get_browser()

    assert ADMIN_EMAIL in browser.find_by_name('email').first.value

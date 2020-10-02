from behave import when, then, given

from django.contrib.auth.models import User

from features.steps.accounts import create_user


@given(u'a regular user exists')
def create_regular_user(context):
    create_user(
        context,
        username='artist',
        password='artist',
        email='artist@example.com',
        is_staff=False,
        is_superuser=False,
    )


@when(u'I go to my user page')
def step_impl(context):
    browser = context.get_browser()

    browser.click_link_by_text('Users')
    browser.click_link_by_text(context.username)


@then(u'I should be logged in')
def step_impl(context):
    # TODO
    pass


@when(u'I enter my username and password')
def step_impl(context):
    browser = context.get_browser()

    browser.find_by_name('login').fill(context.username)
    browser.find_by_name('password').fill(context.password)
    browser.find_by_value('Log In').first.click()


@then(u'I should see the email address I chose')
def step_impl(context):
    # TODO
    pass

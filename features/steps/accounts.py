from behave import when, then
from django.core import mail
from django.contrib.auth.models import User
from allauth.account.models import EmailConfirmationHMAC, EmailAddress


USERNAME = 'test'
EMAIL = 'test@test.com'
PASSWORD = 'test123'


@given(r'an unconfirmed account')
def step_impl(context):
    context.user = User.objects.create(username=USERNAME, email=EMAIL)
    context.user.set_password(PASSWORD)
    context.user.save()

    email = EmailAddress.objects.create(user=context.user, verified=False)
    email.send_confirmation()


@given(r'a confirmed account')
def step_impl(context):
    context.user = User.objects.create(username=USERNAME, email=EMAIL)
    context.user.set_password(PASSWORD)
    context.user.save()

    EmailAddress.objects.create(user=context.user, verified=True)


@when(r'I log in')
def step_impl(context):
    browser = context.get_browser()
    browser.visit(context.base_url)
    browser.click_link_by_text('Log In')
    browser.find_by_name('login').fill(USERNAME)
    browser.find_by_name('password').fill(PASSWORD)
    browser.find_by_value('Log In').click()


@when(r'I click the "{link}" link')
def step_impl(context, link):
    context.get_browser().click_link_by_text(link)


@when(r'I fill out the sign up form')
def step_impl(context):
    browser = context.get_browser()

    browser.find_by_name('username').fill(USERNAME)
    browser.find_by_name('email').fill(EMAIL)
    browser.find_by_name('password1').fill(PASSWORD)
    browser.find_by_name('password2').fill(PASSWORD)


@when(r'I fill out the sign up form without an email')
def step_impl(context):
    browser = context.get_browser()

    browser.find_by_name('username').fill(USERNAME)
    browser.find_by_name('password1').fill(PASSWORD)
    browser.find_by_name('password2').fill(PASSWORD)


@when(r'I click the "{button}" button')
def step_impl(context, button):
    context.get_browser().find_by_value(button).click()


@when(r'I go to the email confirmation URL')
def step_impl(context):
    email = EmailAddress.objects.get(user=context.user)
    confirmation = EmailConfirmationHMAC(email)
    context.get_browser().visit(
        context.base_url +
        '/accounts/confirm-email/{}/'.format(confirmation.key)
    )


@then(r'a new user should be created')
def step_impl(context):
    assert User.objects.get(username=USERNAME) is not None


@then(r'no new user should be created')
def step_impl(context):
    assert len(User.objects.all()) == 0


@then(r'a confirmation email should be sent')
def step_impl(context):
    assert len(mail.outbox) == 1


@then(r'I should see the email confirmation notice')
def step_impl(context):
    assert context.get_browser().is_text_present('confirm your email')


@then(r'my email should be confirmed')
def step_impl(context):
    EmailAddress.objects.filter(user=context.user, verified=True).exists()


@then(r'I should be taken to the dashboard')
def step_impl(context):
    assert context.get_browser().url.endswith('/dashboard/')


@then(r'I should see a message saying "{text}"')
def step_impl(context, text):
    assert text in context.get_browser().find_by_id('messages').text

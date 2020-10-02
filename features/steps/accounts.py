from behave import when, then, given
from django.core import mail
from django.contrib.auth.models import User
from allauth.account.models import EmailConfirmationHMAC, EmailAddress


def create_user(context, username, password, email, **options):
    """Create a user account."""
    context.username = username
    context.password = password
    context.email = email

    context.user = User.objects.create_user(
        username=context.username,
        password=context.password,
        email=context.email,
        **options,
    )


@given(r'an unconfirmed account')
def step_impl(context):
    create_user(
        context,
        username='test',
        password='test123',
        email='test@test.com',
    )

    email = EmailAddress.objects.create(user=context.user, verified=False)
    email.send_confirmation()


@given(r'a confirmed account')
def step_impl(context):
    create_user(
        context,
        username='test',
        password='test123',
        email='test@test.com',
    )

    EmailAddress.objects.create(user=context.user, verified=True)


@when(r'I log in')
def step_impl(context):
    browser = context.get_browser()
    browser.visit(context.base_url)
    browser.click_link_by_text('Log In')
    browser.find_by_name('login').fill(context.username)
    browser.find_by_name('password').fill(context.password)
    browser.find_by_value('Log In').click()


@when(r'I fill out the sign up form')
def step_impl(context):
    browser = context.get_browser()

    context.username = 'test'
    context.password = 'test123'
    context.email = 'test@test.com'

    browser.find_by_name('username').fill(context.username)
    browser.find_by_name('email').fill(context.email)
    browser.find_by_name('password1').fill(context.password)
    browser.find_by_name('password2').fill(context.password)


@when(r'I fill out the sign up form without an email')
def step_impl(context):
    browser = context.get_browser()

    browser.find_by_name('username').fill('test')
    browser.find_by_name('password1').fill('hello')
    browser.find_by_name('password2').fill('hello')


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
    assert User.objects.get(username=context.username) is not None


@then(r'no new user should be created')
def step_impl(context):
    assert len(User.objects.all()) == 0


@then(r'a confirmation email should be sent')
def step_impl(context):
    assert len(mail.outbox) == 1


@then(r'my email should be confirmed')
def step_impl(context):
    EmailAddress.objects.filter(user=context.user, verified=True).exists()


@then(r'I should be taken to {url}')
def step_impl(context, url):
    assert context.get_browser().url.endswith(url)


@then(r'I should see a message saying "{text}"')
def step_impl(context, text):
    assert text in context.get_browser().find_by_id('messages').text

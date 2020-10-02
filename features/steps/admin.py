from behave import when, then, given

from django.contrib.auth.models import User

from features.steps.accounts import create_user


@given(u'an admin user exists')
def create_admin_user(context):
    create_user(
        context,
        username='admin',
        password='admin',
        email='admin@example.com',
        is_staff=True,
        is_superuser=True,
    )

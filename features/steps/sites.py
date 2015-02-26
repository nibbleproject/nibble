import requests
from behave import when, then


@when(u'I go to the site on a different domain')
def step_impl(context):
    context.response = requests.get(
        context.base_url,
        headers={'Host': 'butt.com'},
    )


@then(u'the request should succeed')
def step_impl(context):
    assert context.response.ok

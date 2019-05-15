from behave import when, then


@when(u'I visit the homepage')
def step_impl(context):
    context.get_browser().visit(context.remote_url)


@then(u'the page should load')
def step_impl(context):
    assert 'Nibble' in context.get_browser().title

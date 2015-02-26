from behave import when, then


@when(u'I go to the home page')
def step_impl(context):
    context.get_browser().get(context.base_url)

@then(u'I should see "{text}" in the title')
def step_impl(context, text):
    browser = context.get_browser()

    assert text in browser.title

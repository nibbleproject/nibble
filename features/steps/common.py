from behave import when


@when(u'I go to the path {path}')
def step_impl(context, path):
    context.get_browser().visit(context.base_url + path)


@then(r'I should be taken to {path}')
def step_impl(context, path):
    assert context.get_browser().url.endswith(path)


@when(r'I click the "{link}" link')
def step_impl(context, link):
    context.get_browser().click_link_by_text(link)


@when(r'I click the "{button}" button')
def step_impl(context, button):
    context.get_browser().find_by_value(button).click()

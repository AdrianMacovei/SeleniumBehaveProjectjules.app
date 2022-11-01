from behave import *
from time import sleep


@given(u'I am on the sign-in page')
def step_impl(context):
    context.sign_in_page.go_to_page()


@when(u'I click the sign-up link')
def step_impl(context):
    context.sign_in_page.click_sign_up_link()


@then(u'I am redirected to the sign-up page')
def step_impl(context):
    context.sign_up_page.verify_url


@when(u'I enter "{email}" in email field')
def step_impl(context, email):
    context.sign_in_page.enter_data_in_email_field(email)


@when(u'I enter "{password}" in password field')
def step_impl(context, password):
    context.sign_in_page.enter_data_in_pwd_field(password)


@then(u'Login button should not be enable')
def step_impl(context):
    assert context.sign_in_page.is_login_button_enable() == False


@then(u'A red message with text "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.sign_in_page.warning_message_text()


@then(u'I am redirected to the search all page')
def step_impl(context):
    sleep(3)
    assert context.browser.get_current_url() == context.search_all_page.URL


@then(u'The page title will be "Search"')
def step_impl(context):
    assert context.search_all_page.get_page_title()


@when(u'I click login button')
def step_impl(context):
    context.sign_in_page.click_login_button()


@when(u'I delete the password')
def step_impl(context):
    context.sign_in_page.delete_password()


@then(u'A flash message with text "Invalid email/password combination" appears')
def step_impl(context):
    context.sign_in_page.get_flash_message_text()


@when(u'I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_password()


@then(u'I am redirected to the forgot password page')
def step_impl(context):
    assert context.browser.get_current_url() == context.forgot_password_page.URL

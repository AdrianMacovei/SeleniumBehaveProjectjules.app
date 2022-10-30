from behave import *
from time import sleep


@given(u'I am on the sign-up page')
def go_sign_up_page(context):
    context.sign_up_page.go_to_page()


@when(u'I click personal')
def step_impl(context):
    context.sign_up_page.click_personal_account()


@when(u'I click continue')
def step_impl(context):
    context.sign_up_page.click_continue()


@when(u'I enter "{first_name}" in first name field')
def step_impl(context, first_name):
    context.sign_up_page.enter_data(first_name)


@when(u'I enter "{last_name}" in last name field')
def step_impl(context, last_name ):
    context.sign_up_page.enter_data(last_name)


@when(u'I enter "{email}" in the email field')
def step_impl(context, email):
    context.sign_up_page.enter_data(email)


@then(u'A message with text "{text}" is displayed')
def step_impl(context, text):
    assert context.sign_up_page.is_warning_message_displayed()[0]
    assert context.sign_up_page.is_warning_message_displayed()[1] == text


@then(u'A message with text "Please enter a valid email address." is not displayed')
def step_impl(context):
    assert context.sign_up_page.is_warning_message_displayed()[0] == False

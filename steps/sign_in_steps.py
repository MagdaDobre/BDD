from behave import *

@given('signin: I am a user on Jules sign-in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@when('signin: I fill in a email "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@when('signin: I check the password error message is not displayed')
def step_impl(context):
    context.sign_in_page.verify_password_error_message()

@then('signin: I check the button login is disabled')
def step_impl(context):
    context.sign_in_page.verify_login_button_disabled()


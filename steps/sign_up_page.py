from behave import *
from time import sleep

# test2
@when('signin: I will click on sign_up link')
def set_impl(context):
    context.sign_up_page.click_sign_up_link()

@then("singup: I check if I'm on the right url sign-up")
def set_impl(context):
    context.sign_up_page.verify_url_signup()

@when('singup: I will click on login link')
def set_impl(context):
    context.sign_up_page.click_login_link()

@then("singup: I check if I'm on the right url sign-in")
def set_impl(context):
    context.sign_up_page.verify_url_sign_in()


# test3

@when('signup: I select the Personal button ratio')
def set_impl(context):
    context.sign_up_page.select_ratio_personal()
    sleep(1)

@when('signup: I click on continue button')
def set_impl(context):
    context.sign_up_page.click_continue_button()
    sleep(3)

@when('signup: I enter my first name "{firstname}"')
def set_impl(context, firstname):
    context.sign_up_page.set_first_name(firstname)

@when('signup: I enter my last name "{lastname}"')
def set_impl(context, lastname):
    context.sign_up_page.set_last_name(lastname)

@when('signup: I enter email "{email}"')
def set_impl(context, email):
    context.sign_up_page.set_email(email)
    sleep(3)

@When('signup: I verify the email error message is diplayed "{msg}"')
def set_impl(context, msg):
    context.sign_up_page.verify_email_error_msg(msg)

@When('signup: I clear the input email')
def set_impl(context):
    context.sign_up_page.clear_email_input()

@When('signup: I enter the correct email "{email}"')
def set_impl(context, email):
    context.sign_up_page.set_email(email)

@Then('signup: I verify the email error message is not diplayed "{notif}"')
def set_impl(context, notif):
    context.sign_up_page.verify_email_error_msg(notif)


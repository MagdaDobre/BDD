from browser import Browser
from base_page1 import BasePage
from pages.sign_in_page import SignInPage
from pages.sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.base_page1 = BasePage()
    context.sign_in_page = SignInPage()
    context.sign_up_page = SignUpPage()


def after_all(context):
    context.browser.close()


from browser import Browser
from pages.sign_up_page import SignUpPage
from pages.sign_in_page import SignInPage
from pages.forgot_password_page import ForgotPwdPage
from pages.search_all_page import SearchPage


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = SignInPage(context.browser.driver)
    context.sign_up_page = SignUpPage(context.browser.driver)
    context.forgot_password_page = ForgotPwdPage(context.browser.driver)
    context.search_all_page = SearchPage(context.browser.driver)


def after_all(context):
    context.browser.close()

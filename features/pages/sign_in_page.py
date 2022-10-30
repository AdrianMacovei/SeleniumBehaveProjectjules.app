from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from features.pages.base_page import BasePage


class SignInPage(BasePage):

    URL = "https://jules.app/sign-in"
    LOGIN_SELECTOR = (By.XPATH, "//button[@type='submit']")
    PWD_FIELD_SELECTOR = (By.XPATH, "//input[@placeholder='Enter your password']")

    def click_sign_up_link(self):
        sign_up_selector = (By.XPATH, "//a[contains(text(),'Sign up.')]")
        self.driver.find_element(*sign_up_selector).click()

    def enter_data_in_email_field(self, email):
        email_field_selector = (By.XPATH, "//input[@placeholder='Enter your email']")
        self.driver.find_element(*email_field_selector).send_keys(email)

    def enter_data_in_pwd_field(self, password):
        self.driver.find_element(*SignInPage.PWD_FIELD_SELECTOR).send_keys(password)

    def is_login_button_enabled(self):
        return self.driver.find_element(*SignInPage.LOGIN_SELECTOR).is_enabled()

    def warning_message_text(self):
        return self.driver.find_element(By.TAG_NAME, "p").text

    def click_login_button(self):
        if self.driver.find_element(*SignInPage.LOGIN_SELECTOR).is_enabled():
            self.driver.find_element(*SignInPage.LOGIN_SELECTOR).click()

    def delete_password(self):
        pwd = self.driver.find_element(*SignInPage.PWD_FIELD_SELECTOR)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)

    def get_flash_message_text(self):
        flash_message = (By.XPATH, "//span[contains(text(),'Invalid email/password combination')]")
        return self.driver.find_element(*flash_message).text

    def click_forgot_password(self):
        self.driver.find_element(by=By.LINK_TEXT, value="Forgot password?").click()
from selenium.webdriver.common.by import By
from time import sleep
from features.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SignUpPage(BasePage):

    URL = "https://jules.app/sign-up"

    def click_personal_account(self):
        sleep(1)
        personal_selector = (By.XPATH, "//input[@value='personal']")
        self.driver.find_element(*personal_selector).click()

    def click_continue(self):
        element = self.driver.find_element(By.XPATH, "//span[contains(text(),'CONTINUE')]")
        element.click()
        sleep(1)

    def enter_data(self, value):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type your answer here...']").send_keys(value)

    def is_warning_message_displayed(self):
        warning_message_selector = (By.XPATH, "//p[contains(text(),'Please enter a valid email address.')]")
        try:
            displayed = self.driver.find_element(*warning_message_selector).is_displayed()
        except NoSuchElementException as e:
            displayed = False

        if displayed:
            text = self.driver.find_element(*warning_message_selector).text
        else:
            text = "NoSuchElement"
        return displayed, text

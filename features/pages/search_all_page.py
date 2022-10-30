from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchPage(BasePage):

    URL = "https://jules.app/search/all"

    def get_page_title(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]").text

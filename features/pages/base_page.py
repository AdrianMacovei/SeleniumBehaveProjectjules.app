
class BasePage:

    URL = ""

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get(self.URL)

    def verify_url(self):
        assert self.driver.get_curent_url() == self.URL

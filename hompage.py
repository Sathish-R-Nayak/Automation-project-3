from lib import SeleniumWrapper

class HomePage(SeleniumWrapper):

    def __init__(self, driver):
        self.driver=driver

    def click_login(self):
        self.click_element(("link text","Log in"))

    def click_registration(self):
        self.click_element(("link text","Register"))


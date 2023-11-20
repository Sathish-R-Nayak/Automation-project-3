from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement

class _visibility_of_element_located(visibility_of_element_located):

    def __call__(self, driver):
        result=super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False

def please_wait(func):
    def wrapper(*args,**kwargs):
        instnace=args[0]
        locator=args[1]
        w=WebDriverWait(instnace.driver,20)
        v=_visibility_of_element_located(locator)
        w.until(v)
        return func(*args,**kwargs)
    return wrapper

class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
   
    @please_wait
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @please_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @please_wait
    def select_item(self,locator,item):
        element=self.driver.find_element(*locator)
        s=Select(element)
        if isinstance(item,str):
            s.select_by_visible_text(item)
        else:
            s.select_by_index(item)




        
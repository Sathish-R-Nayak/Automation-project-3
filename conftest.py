from selenium.webdriver import Chrome
import pytest
from time import sleep

@pytest.fixture()
def setup_tear_down():
    driver=Chrome("D:\\chrome\\chromedriver-win64\\chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.close()

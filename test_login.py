from lib import SeleniumWrapper
from loginpage import LoginPage
import pytest
from hompage import HomePage
from xl_lib import read_data


headers="email,password"

data=read_data("smoke","test_login_positive")

@pytest.mark.parametrize(headers,data)
def test_login(setup_tear_down,email,password):

    #sw=SeleniumWrapper(setup_tear_down)

    hp=HomePage(setup_tear_down)
    hp.click_login()
    #sw.click_element(("link text","Log in"))

    lp=LoginPage(setup_tear_down)

    lp.Login(email,password)



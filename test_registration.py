from lib import SeleniumWrapper
from registration import Registration
import pytest
from hompage import HomePage
from xl_lib import read_data

headers="gender,fname,lname,email,pwd"

data=read_data("smoke","test_registration")
@pytest.mark.parametrize(headers,data)
def test_registration(setup_tear_down,gender,fname,lname,email,pwd):
    sw=SeleniumWrapper(setup_tear_down)

    hp=HomePage(setup_tear_down)
    hp.click_registration()
    #sw.click_element(("link text","Register"))

    rp=Registration(setup_tear_down)
    
    rp.registration(gender,fname,lname,email,pwd)
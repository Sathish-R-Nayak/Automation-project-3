from lib import SeleniumWrapper
from xl_lib import read_locators

class LoginPage:
    
    #login_page_objects={"txt_email":('id','Email'),
    #                   "txt_password":('id','Password'),
    #                  "btn_login":("xpath","//input[@value='Log in']")
    #                 }

    login_page_objects=read_locators("loginpage")


    def __init__(self,driver):
        self.driver=driver

    def Login(self,email,password):

        sw=SeleniumWrapper(self.driver)

        sw.enter_text(LoginPage.login_page_objects['txt_email'],value=email)
        sw.enter_text(LoginPage.login_page_objects['txt_password'],value=password)
        sw.click_element(LoginPage.login_page_objects['btn_login'])



             
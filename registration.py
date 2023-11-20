from lib import SeleniumWrapper
from xl_lib import read_locators

class Registration:
    #registration_page_objects={"rdo_male":('id','gender-male'),
    #                           "rdo_female":('id','gender-female'),
    #                           "txt_fname":('id','FirstName'),
    #                           "txt_lname":('id','LastName'),
    #                           "txt_email":('id','Email'),
    #                           "txt_password":('id','Password'),
    #                           "txt_confirm_password":('id','ConfirmPassword')}

    registration_page_objects=read_locators("registrationpage")

    def __init__(self,driver):
        self.driver=driver

    def registration(self,gender,fname,lname,email,pwd):

        sw=SeleniumWrapper(self.driver)

        if gender=="Male":
            
            sw.click_element(Registration.registration_page_objects['rdo_male'])
        
        else:
            
            sw.click_element(Registration.registration_page_objects['rdo_female'])        
        
        sw.enter_text(Registration.registration_page_objects['txt_fname'],value=fname)
        sw.enter_text(Registration.registration_page_objects['txt_lname'],value=lname)
        sw.enter_text(Registration.registration_page_objects['txt_email'],value=email)
        sw.enter_text(Registration.registration_page_objects['txt_password'],value=pwd)





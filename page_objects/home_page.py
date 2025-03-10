import time

from selenium.webdriver.common.by import By


class HomePage:

    # locators
    lnk_signin_lnk_txt = "Sign in"
    lin_signout_xpath ='//a[normalize-space()="Sign out"]'

    # constructor
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
    # action methods

    def click_Signin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_signin_lnk_txt).click()

    def click_Signout(self):
        self.driver.find_element(By.XPATH,self.lin_signout_xpath).click()



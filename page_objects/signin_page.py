from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SigninPage:

    # locators
    inp_email_create_id = "email_create"
    btn_create_account_id ="SubmitCreate"
    txt_mail_error_id = "create_account_error"
    inp_email_signin_id = "email"
    inp_password_signin_id = "passwd"
    btn_signin_id = "SubmitLogin"

    def __init__(self,driver):
        self.driver = driver


    # action methods



    def set_create_email(self,email):
        self.driver.find_element(By.ID,self.inp_email_create_id).send_keys(email)

    def click_create_account(self):
        self.driver.find_element(By.ID,self.btn_create_account_id).click()

    def set_signin_email(self,email):
        self.driver.find_element(By.ID,self.inp_email_signin_id).send_keys(email)

    def set_signin_password(self,password):
        self.driver.find_element(By.ID,self.inp_password_signin_id).send_keys(password)

    def click_signin(self):
        self.driver.find_element(By.ID,self.btn_signin_id).click()





    def is_navigated_to_create_account(self):
        try:
            wait =WebDriverWait(self.driver,timeout=10,poll_frequency=2)
            element = wait.until(EC.visibility_of_element_located((By.ID,self.txt_mail_error_id)))
            return False
        except Exception as e:
            print(e)
            return True

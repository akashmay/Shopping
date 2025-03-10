from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class AccountCreatePage:

    # locators
    redio_male_id = "id_gender1"
    redio_female_id = "id_gender2"
    inp_firstname_id = "customer_firstname"
    inp_lastname_id = "customer_lastname"
    inp_password_id = "passwd"
    drp_day_id = "days"
    drp_month_id = "months"
    drp_year_id = "years"
    ckb_newsletter_id ="newsletter"
    btn_register_id = "submitAccount"

    # constructor
    def __init__(self,driver):
        self.driver =  driver

    # action methods
    def check_gender(self,gender):
        if gender=="male":
            self.driver.find_element(By.ID,self.redio_male_id).click()
        elif gender == "female":
            self.driver.find_element,(By.ID,self.redio_female_id).click()

    def set_firstname(self,firstname):
        self.driver.find_element(By.ID,self.inp_firstname_id).send_keys(firstname)

    def set_lastname(self,lastname):
        self.driver.find_element(By.ID,self.inp_lastname_id).send_keys(lastname)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.inp_password_id).send_keys(password)


    def set_date(self,date):
        drp_element = Select(self.driver.find_element(By.ID,self.drp_day_id))
        drp_element.select_by_value(date)

    def set_month(self,month):
        drp_element = Select(self.driver.find_element(By.ID,self.drp_month_id))
        drp_element.select_by_value(month)
        drp_element.select_by_value(month)


    def set_year(self,year):
        drp_element = Select(self.driver.find_element(By.ID,self.drp_year_id))
        drp_element.select_by_value(year)

    def signup_newsletter(self):
        self.driver.find_element(By.ID,self.ckb_newsletter_id).click()

    def click_register(self):
        self.driver.find_element(By.ID,self.btn_register_id).click()



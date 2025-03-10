import os.path
import time

from colorama.ansi import clear_screen

from page_objects.home_page import HomePage
from page_objects.signin_page import SigninPage
from page_objects.account_create_page import AccountCreatePage
from utilities.random_string import Random_string
from utilities.read_properties import ReadProperties
from utilities.custom_logging import LogGen
from utilities.excel_utiles import ExcelUtiles
from utilities.db_utils import DbConnect


class TestAccountRegistration():

    def test_account_registration(self,setup):

        conn = DbConnect.connect_to_db("test_db")
        cur = conn.cursor()

        for i in range(2,22):
            self.driver = setup
            self.driver.implicitly_wait(10)
            self.driver.maximize_window
            self.url = ReadProperties.read_base_url()
            self.logger = LogGen.get_logger()

            self.home_page = HomePage(self.driver)
            self.signin_page = SigninPage(self.driver)
            self.account_create_page = AccountCreatePage(self.driver)
            self.excel_file_name = ReadProperties.read_excel_created_accounts_path()

            self.driver.get(self.url)
            self.logger.critical(msg="Launched url............")
            self.home_page.click_Signin()
            email = Random_string() + "@gmail.com"
            self.signin_page.set_create_email(email)
            self.signin_page.click_create_account()
            is_navigated = self.signin_page.is_navigated_to_create_account()
            if is_navigated:
                self.account_create_page.check_gender("male")
                self.account_create_page.set_firstname("Akash")
                self.account_create_page.set_lastname("Mans")
                self.account_create_page.set_password("test@25!")
                self.account_create_page.set_date("21")
                self.account_create_page.set_month("12")
                self.account_create_page.set_year("1993")
                self.account_create_page.signup_newsletter()
                self.account_create_page.click_register()
                self.logger.debug("Test completed.........")
                #ExcelUtiles.write_to_cell(self.excel_file_name,"Sheet1",i, 1, email)
                cur.execute("INSERT INTO login (email, password) VALUES (%s, %s)", (email, "test@25!"))
                #ExcelUtiles.write_to_cell(self.excel_file_name,"Sheet1",i, 2, "test@25!")
                conn.commit()
                self.home_page.click_Signout()
            else:
                self.driver.save_screenshot(os.path.abspath(os.path.curdir) + "\\screenshots\\sc1.png")









        

from fileinput import filename

import allure
import pytest
from allure_commons.types import AttachmentType

from page_objects.home_page import HomePage
from page_objects.signin_page import SigninPage
from utilities.db_utils import DbConnect
from utilities.excel_utiles import ExcelUtiles
from utilities.read_properties import ReadProperties


class TestAccountLogin:

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_account_login(self,setup):

        self.excel_created_accounts_path = ReadProperties.read_excel_created_accounts_path()
        conn = DbConnect.connect_to_db("test_db")
        cur = conn.cursor()
        cur.execute("select email,password from login")
        self.users = cur.fetchall()


        #for i in range (len(self.users)):
        for i in range(5):


            #self.email = ExcelUtiles.read_from_cell(self.excel_created_accounts_path, "Sheet1", i, 1)
            #self.password = ExcelUtiles.read_from_cell(self.excel_created_accounts_path, "Sheet1", i, 2)
            self.email = self.users[i][0]
            self.password = self.users[i][1]

            self.driver = setup
            url = ReadProperties.read_base_url()
            self.driver.get(url)
            self.home_page = HomePage(self.driver)
            self.signin_page = SigninPage(self.driver)

            self.home_page.click_Signin()
            self.signin_page.set_signin_email(self.email)
            #ExcelUtiles.write_to_cell(self.excel_created_accounts_path, "Text_login", i, 1,self.email)
            self.signin_page.set_signin_password(self.password)
            #ExcelUtiles.write_to_cell(self.excel_created_accounts_path, "Text_login", i, 2,self.password)
            self.signin_page.click_signin()
            allure.attach(self.driver.get_screenshot_as_png(),name="loging_in",attachment_type=AttachmentType.PNG)
            #ExcelUtiles.write_to_cell(self.excel_created_accounts_path, "Text_login", i, 3,"pass")
            #cur.execute("update login set result=%s where email=%s",("pass",self.email) )
            conn.commit()
            self.home_page.click_Signout()





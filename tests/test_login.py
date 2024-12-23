import pytest
from utilities import ExcelReader
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest



class TestLogin(BaseTest):
    data = ExcelReader.get_data_from_excel("C:/Users/srinivas_lankela/PycharmProjects/pytest/TestPytestSelenium/ExcelFiles/test_credentials.xlsx", "LoginTest")
    @pytest.mark.parametrize("email_address,password",data)
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(email_address)
        login_page.enter_password_address(password)
        account_page= login_page.click_on_login_button()
        assert account_page.display_status_of_edit_your_account()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(self.generate_email_with_time_stamp())
        login_page.enter_password_address("Gud_Luck1")
        login_page.click_on_login_button()
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address("lankelasrinivas3@gmail.com")
        login_page.enter_password_address("Gud_Luck12")
        login_page.click_on_login_button()
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(" ")
        login_page.enter_password_address(" ")
        login_page.click_on_login_button()
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning)








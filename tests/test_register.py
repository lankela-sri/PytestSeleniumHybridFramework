from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pytest

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name_input("sri")
        register_page.enter_last_name_input("nivas")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_phone_number("9121467654")
        register_page.enter_pwd("Gud_Luck12")
        register_page.enter_pwd_confirm("Gud_Luck12")
        register_page.click_check_box()
        account_success_page = register_page.click_continue_button()
        expected_heading = "Your Account Has Been Created!"
        assert account_success_page.account_message_created().__contains__(expected_heading)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name_input("sri")
        register_page.enter_last_name_input("nivas")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_phone_number("9121467654")
        register_page.enter_pwd("Gud_Luck12")
        register_page.enter_pwd_confirm("Gud_Luck12")
        register_page.click_subscribe_news_check_box()
        register_page.click_check_box()
        account_success_page = register_page.click_continue_button()
        expected_heading = "Your Account Has Been Created!"
        assert account_success_page.account_message_created().__contains__(expected_heading)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name_input("sri")
        register_page.enter_last_name_input("nivas")
        register_page.enter_email("lankelasrinivas@gmail.com")
        register_page.enter_phone_number("9121467654")
        register_page.enter_pwd("Gud_Luck1")
        register_page.enter_pwd_confirm("Gud_Luck1")
        register_page.click_subscribe_news_check_box()
        register_page.click_check_box()
        register_page.click_continue_button()
        expected_warning = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning)

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name_input("")
        register_page.enter_last_name_input("")
        register_page.enter_email("")
        register_page.enter_phone_number("")
        register_page.enter_pwd("")
        register_page.enter_pwd_confirm("")
        register_page.click_continue_button()
        expected_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_message().__contains__(expected_text)
        expected_first_Name_text = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning_message().__contains__(expected_first_Name_text)
        expected_last_Name_text = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning_message().__contains__(expected_last_Name_text)









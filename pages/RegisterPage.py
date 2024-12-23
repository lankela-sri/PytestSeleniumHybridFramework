from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:
    def __init__(self,driver):

        self.driver = driver

    first_name_input_id = "input-firstname"
    last_name_input_id = "input-lastname"
    email_id = "input-email"
    phone_number_id = "input-telephone"
    pwd_id = "input-password"
    pwd_confirm_id = "input-confirm"
    agree_checkbox_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    subscribe_radio_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname'] /following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname'] /following-sibling::div"

    def enter_first_name_input(self,first_name):
        self.driver.find_element(By.ID, self.first_name_input_id).click()
        self.driver.find_element(By.ID, self.first_name_input_id).clear()
        self.driver.find_element(By.ID, self.first_name_input_id).send_keys(first_name)

    def enter_last_name_input(self,last_name):
        self.driver.find_element(By.ID, self.last_name_input_id).click()
        self.driver.find_element(By.ID, self.last_name_input_id).clear()
        self.driver.find_element(By.ID, self.last_name_input_id).send_keys(last_name)

    def enter_email(self,email_text):
        self.driver.find_element(By.ID, self.email_id).click()
        self.driver.find_element(By.ID, self.email_id).clear()

        self.driver.find_element(By.ID, self.email_id).send_keys(email_text)

    def enter_phone_number(self,number):
        self.driver.find_element(By.ID, self.phone_number_id).click()
        self.driver.find_element(By.ID, self.phone_number_id).clear()
        self.driver.find_element(By.ID, self.phone_number_id).send_keys(number)

    def enter_pwd(self,pwd):
        self.driver.find_element(By.ID, self.pwd_id).click()
        self.driver.find_element(By.ID, self.pwd_id).clear()
        self.driver.find_element(By.ID, self.pwd_id).send_keys(pwd)

    def enter_pwd_confirm(self,pwd_confirm):
        self.driver.find_element(By.ID, self.pwd_confirm_id).click()
        self.driver.find_element(By.ID, self.pwd_confirm_id).clear()
        self.driver.find_element(By.ID, self.pwd_confirm_id).send_keys(pwd_confirm)

    def click_check_box(self):
        self.driver.find_element(By.XPATH, self.agree_checkbox_xpath).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def click_subscribe_news_check_box(self):
        self.driver.find_element(By.XPATH, self.subscribe_radio_xpath).click()

    def retrieve_duplicate_email_warning(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_xpath).text

    def retrieve_privacy_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH,self.first_name_warning_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text






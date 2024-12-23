from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage


class LoginPage:

    def __init__(self,driver):

        self.driver = driver

    email_address_field_id = "input-email"
    password_address_field_id = "input-password"
    login_button_xpath = "//input[@value ='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self,email_address_text):

        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address_text)

    def enter_password_address(self, password_address_text):
        self.driver.find_element(By.ID, self.password_address_field_id).click()
        self.driver.find_element(By.ID, self.password_address_field_id).clear()
        self.driver.find_element(By.ID, self.password_address_field_id).send_keys(password_address_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text






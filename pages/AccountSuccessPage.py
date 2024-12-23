from selenium.webdriver.common.by import By

class AccountSuccessPage:
    def __init__(self,driver):
        self.driver = driver

    account_success_message = "//div[@id='content']/h1"

    def account_message_created(self):
        return self.driver.find_element(By.XPATH, self.account_success_message).text
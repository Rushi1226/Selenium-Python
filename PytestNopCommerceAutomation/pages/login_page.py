import time

from selenium.webdriver.common.by import By

from helpers.selenium_helper import Selenium_helper


class LoginPage(Selenium_helper):
    login_icon_locator =(By.XPATH,"/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")
    user_email_locator = (By.ID, "Email")
    user_password_locator = (By.ID, "Password")
    login_button_locator = (By.XPATH, "//button[normalize-space()='Log in']")

    def user_login(self, email, password):
        self.click(self.login_icon_locator)
        self.enter(self.user_email_locator, email)
        self.enter(self.user_password_locator, password)
        self.click(self.login_button_locator)
        time.sleep(2)

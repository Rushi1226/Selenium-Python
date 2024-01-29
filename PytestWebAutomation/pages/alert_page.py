import time

from selenium.webdriver.common.by import By

from helpers.Selenium_helper import Selenium_helper


class AlertPage(Selenium_helper):
    alert_button_locator = (By.XPATH, "//button[normalize-space()='Alert']")
    confirm_alert_button_locator = (By.XPATH, "//button[normalize-space()='Confirm Box']")
    prompt_button_locator = (By.XPATH, "//button[normalize-space()='Prompt']")

    def __init__(self, driver):
        super().__init__(driver)

    def check_alert(self):
        self.click(self.alert_button_locator)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        assert alert.text == "I am an alert box!"
        time.sleep(2)
        alert.accept()
        time.sleep(3)

    def alert_confirm_box(self):
        self.click(self.confirm_alert_button_locator)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        assert alert.text == "Press a button!"
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def alert_prompt_button(self):
        self.click(self.prompt_button_locator)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

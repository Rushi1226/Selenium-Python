import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from helpers.Selenium_helper import Selenium_helper


class DoubleClick(Selenium_helper):

    def __init__(self, driver):
        super().__init__(driver)

    def check_double_click(self):
        button_locator = self.driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

        field1_locator = self.driver.find_element(By.ID,"field1")
        field2_locator = self.driver.find_element(By.ID,"field2")
        action_chains = ActionChains(self.driver)
        action_chains.double_click(button_locator).perform()

        time.sleep(2)

        text_to_copy = field1_locator.get_attribute("value")
        self.driver.execute_script("arguments[0].value = arguments[1]", field2_locator, text_to_copy)

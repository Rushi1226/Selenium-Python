import logging

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from helpers.constants_helpers import ExplicitWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()


class Selenium_helper:
    def __init__(self,driver):
        self.driver = driver

    def find(self, *locator):
        return WebDriverWait(self.driver, ExplicitWait).until(EC.element_to_be_clickable(*locator))

    def click(self, locator):
        logger.debug("Click on the element")
        WebDriverWait(self.driver, ExplicitWait).until(EC.element_to_be_clickable(locator)).click()

    def enter(self,locator, text):
        logger.debug("Enterning value for the webelement")
        WebDriverWait(self.driver,ExplicitWait).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def get_text(self,locator):
        logger.debug("Getting text for the element")
        return WebDriverWait(self.driver, ExplicitWait).until(EC.visibility_of_element_located(locator)).text

    def clear_text(self, locator):
        logger.debug("Clearing the text field")
        WebDriverWait(self.driver,ExplicitWait).until(EC.element_to_be_clickable(locator)).clear()

    def get_list(self, locator):
        logger.debug("Getting a list of webelement")
        try:
            element = WebDriverWait(self.driver, ExplicitWait).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            element = []

        return element




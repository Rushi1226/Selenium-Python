import time

from selenium.webdriver.common.by import By

from helpers.selenium_helper import Selenium_helper
from selenium.webdriver.support.ui import Select


class ShoppingCart(Selenium_helper):
    shopping_cart_button_locator = (By.ID, "topcartlink")
    gift_wrapping_dropdown_locator = (By.ID, "checkout_attribute_1")
    terms_checkbox_locator = (By.ID, "termsofservice")
    checkout_button_locator = (By.ID, "checkout")
    close_message_locator = (By.XPATH, "//*[@id='bar-notification']/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def shopping_cart_checkout(self, gift_wrap):
        self.click(self.close_message_locator)
        time.sleep(1)
        self.click(self.shopping_cart_button_locator)

        gift_wrapping = self.find(self.gift_wrapping_dropdown_locator)
        gift_wrapping_selector = Select(gift_wrapping)
        gift_wrapping_selector.select_by_value(gift_wrap)

        self.click(self.terms_checkbox_locator)
        self.click(self.checkout_button_locator)

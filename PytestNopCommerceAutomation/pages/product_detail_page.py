from selenium.webdriver.common.by import By

from helpers.selenium_helper import Selenium_helper
from selenium.webdriver.support.ui import Select


class ProductPage(Selenium_helper):
    click_product_locator = (By.XPATH, "//h2/a[contains(text(),'Build your own computer')]")
    processor_dropdown_locator = (By.ID, "product_attribute_1")
    ram_dropdown_locator = (By.ID, "product_attribute_2")
    hdd_radio_button_locator = (By.ID, "product_attribute_3_7")
    os_radio_button_locator = (By.ID, "product_attribute_4_9")
    software_checkbox_locator = (By.ID, "product_attribute_5_10")
    product_quantity_locator = (By.ID, "product_enteredQuantity_1")
    add_to_cart_button_locator = (By.ID, "add-to-cart-button-1")
    success_message_locator = (By.CSS_SELECTOR, ".bar-notification.success .content")

    def __init__(self, driver):
        super().__init__(driver)

    def product_details_page(self, processor, ram, quantity):
        self.click(self.click_product_locator)
        processor_dropdown = self.find(self.processor_dropdown_locator)
        processor_selector = Select(processor_dropdown)
        processor_selector.select_by_value(processor)

        ram_dropdown = self.find(self.ram_dropdown_locator)
        ram_selector = Select(ram_dropdown)
        ram_selector.select_by_value(ram)

        # Handle HDD radio button
        self.click(self.hdd_radio_button_locator)

        # Handle OS radio button
        self.click(self.os_radio_button_locator)

        # Handle Software checkbox
        self.click(self.software_checkbox_locator)

        self.clear_text(self.product_quantity_locator)
        self.enter(self.product_quantity_locator, quantity)

        self.click(self.add_to_cart_button_locator)

        success_message = self.find(self.success_message_locator)
        print("Success Message : ", success_message.text)

from selenium.webdriver.common.by import By

from helpers.selenium_helper import Selenium_helper
from selenium.webdriver.support.ui import Select
from configuration.config import TestData




class CheckoutPage(Selenium_helper):
    first_name_locator = (By.ID, "Rushikesh ")
    last_name_locator = (By.ID, "Kadam")
    EMAIL_INPUT = (By.ID, "rushik@gmail.com")

    country_dropdown_locator = (By.ID, "BillingNewAddress_CountryId")
    state_dropdown_locator = (By.ID, "BillingNewAddress_StateProvinceId")
    city_locator = (By.ID, "BillingNewAddress_City")
    address_locator = (By.ID, "BillingNewAddress_Address1")
    zip_code_locator = (By.ID, "BillingNewAddress_ZipPostalCode")
    phone_locator = (By.ID, "BillingNewAddress_PhoneNumber")
    continue_button_locator = (By.XPATH, "//input[@value='Continue']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_shipping_address(self, country, state, city, address, postal_code, phone):
        country_dropdown = self.find(self.country_dropdown_locator)
        country_selector = Select(country_dropdown)
        country_selector.select_by_visible_text(country)

        state_dropdown = self.find(self.state_dropdown_locator)
        state_selector = Select(state_dropdown)
        state_selector.select_by_visible_text(state)

        self.enter(self.city_locator,city)
        self.enter(self.address_locator,address)
        self.enter(self.zip_code_locator,postal_code)
        self.enter(self.phone_locator,phone)

        self.click(self.continue_button_locator)
















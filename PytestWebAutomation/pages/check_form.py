import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from helpers.Selenium_helper import Selenium_helper


class CheckForm(Selenium_helper):
    name_locator = (By.ID, "name")
    email_locator = (By.ID, "email")
    phone_locator = (By.ID, "phone")
    address_locator = (By.ID, "textarea")
    gender_radio_locator = (By.ID, "male")
    days_checkbox_locator = (By.ID, "sunday")
    select_country_locator = (By.ID, "country")
    select_colors_locator = (By.ID, "colors")
    select_date_locator = (By.ID, "datepicker")
    link_locator = (By.XPATH, "//*[@id='post-body-1307673142697428135']/a[1]")
    get_value_from_table_locator = (By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[5]/td[3]")
    select_table_checkbox_locator = (By.XPATH, "//*[@id='productTable']/tbody/tr[1]/td[4]/input")

    def __init__(self, driver):
        super().__init__(driver)

    def automation_practice_form(self, name, email, phone, address, country, color, date):
        self.click(self.name_locator)
        self.enter(self.name_locator, name)
        self.click(self.email_locator)
        self.enter(self.email_locator, email)
        self.click(self.phone_locator)
        self.enter(self.phone_locator, phone)
        self.click(self.address_locator)
        self.enter(self.address_locator, address)
        self.click(self.gender_radio_locator)
        self.click(self.days_checkbox_locator)

        country_dropdown = self.find(self.select_country_locator)
        select_country = Select(country_dropdown)
        select_country.select_by_value(country)

        color_dropdown = self.find(self.select_colors_locator)
        select_color = Select(color_dropdown)
        select_color.select_by_value(color)

        self.click(self.select_date_locator)
        self.enter(self.select_date_locator, date)

        # self.click(self.link_locator)

        get_value = self.get_text(self.get_value_from_table_locator)
        print("Table Value :", get_value)

        self.click(self.select_table_checkbox_locator)

        time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from helpers.Selenium_helper import Selenium_helper


class ResizablePage(Selenium_helper):

    def __init__(self, driver):
        super().__init__(driver)

    def check_resizable_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".ui-resizable-handle.ui-resizable-e")

        initial_size = element.size

        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(element).move_by_offset(50, 50).release().perform()

        final_size = element.size

        if final_size != initial_size:
            print("Resize action successful!")
        else:
            print("Resize action failed!")

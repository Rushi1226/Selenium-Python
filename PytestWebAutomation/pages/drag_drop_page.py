from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from helpers.Selenium_helper import Selenium_helper


class DragDrop(Selenium_helper):

    def __init__(self, driver):
        super().__init__(driver)

    def check_drag_drop(self):
        drag_element = self.driver.find_element(By.XPATH,"//div[@id='draggable']")
        target_element = self.driver.find_element(By.XPATH,"//div[@id='droppable']")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, target_element).perform()

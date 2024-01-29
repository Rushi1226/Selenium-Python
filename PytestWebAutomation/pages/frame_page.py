import time

from selenium.webdriver.common.by import By

from helpers.Selenium_helper import Selenium_helper


class FramePage(Selenium_helper):

    def __init__(self, driver):
        super().__init__(driver)

    def check_frame_page(self):
        element_locator = (By.ID,"RESULT_TextField-0")
        self.driver.switch_to.frame("frame-one796456169")
        # element =  self.find(By.ID,"RESULT_TextField-0")
        self.enter(element_locator, "Rushikesh")





        time.sleep(3)

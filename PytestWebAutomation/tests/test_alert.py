from pages.alert_page import AlertPage
from tests.base_test import BaseTest


class TestAlertPage(BaseTest):

    def test_alert_button(self):
        alert_page = AlertPage(self.driver)
        alert_page.check_alert()

    def test_confirm_alert_box(self):
        alert_page = AlertPage(self.driver)
        alert_page.alert_confirm_box()

    def test_prompt_button(self):
        alert_page = AlertPage(self.driver)
        alert_page.alert_prompt_button()

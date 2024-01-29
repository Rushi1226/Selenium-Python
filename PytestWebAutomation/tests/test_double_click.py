from pages.double_click_page import DoubleClick
from tests.base_test import BaseTest


class TestDoubleClick(BaseTest):

    def test_double_click(self):
        double_click = DoubleClick(self.driver)
        double_click.check_double_click()

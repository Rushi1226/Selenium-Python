from pages.resizable_page import ResizablePage
from tests.base_test import BaseTest


class TestResizable(BaseTest):

    def test_resizable_page(self):

        resizable = ResizablePage(self.driver)
        resizable.check_resizable_page()



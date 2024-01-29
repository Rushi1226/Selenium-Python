from pages.frame_page import FramePage
from tests.base_test import BaseTest


class TestFramePage(BaseTest):

    def test_frame(self):
        check_frame = FramePage(self.driver)
        check_frame.check_frame_page()
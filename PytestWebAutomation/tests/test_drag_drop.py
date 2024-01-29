from pages.drag_drop_page import DragDrop
from tests.base_test import BaseTest


class TestDragDrop(BaseTest):

    def test_drag_drop(self):
        drag_drop = DragDrop(self.driver)
        drag_drop.check_drag_drop()

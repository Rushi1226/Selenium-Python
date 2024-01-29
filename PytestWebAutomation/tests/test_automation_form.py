from pages.check_form import CheckForm
from tests.base_test import BaseTest
from configuration.config import TestData


class TestAutomationFormPractice(BaseTest):

    def test_form_demo(self):
        ch = CheckForm(self.driver)
        ch.automation_practice_form(
            TestData.Name,
            TestData.Email,
            TestData.Phone,
            TestData.Address,
            TestData.Country,
            TestData.Color,
            TestData.Date
        )
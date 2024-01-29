from pages.login_page import LoginPage
from tests.base_test import BaseTest

from configuration.config import TestData


class TestLogin(BaseTest):

    def test_valid_user_login(self):
        print("in test login function")
        login = LoginPage(self.driver)
        login.user_login(TestData.LOGIN_EMAIL, TestData.LOGIN_PASSWORD)

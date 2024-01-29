import pytest
from selenium import webdriver
from helpers.constants_helpers import ExplicitWait, url, ImplicitWait


@pytest.fixture()
def driver_setup(request):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(ImplicitWait)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
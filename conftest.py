import pytest
from appium import webdriver
from page_objects.base_page import BasePageObject


@pytest.fixture(scope='function')
def driver():
    desired_capabilities = {"app": "C:\\Users\\anduser\\AppData\\Local\\Reverso\\Reverso\\Reverso.exe"}
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=desired_capabilities)
    yield driver
    driver.close_app()
    BasePageObject(driver).accept_alert()

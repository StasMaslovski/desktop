import pytest
from appium import webdriver
from page_objects.base_page import BasePageObject
import allure
import os
from config import Config


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Remote(
        command_executor=Config.command_executor.value,
        desired_capabilities=Config.desired_capabilities.value)
    yield driver
    driver.close_app()
    BasePageObject(driver).accept_alert()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
         get the hook function for the state of each use case
        :param item:  test case
        :param call:  test procedure
        :return:
        """
    #  get the result of the call to the hook method
    outcome = yield
    rep = outcome.get_result()  # get the test report from the result of the call to the hook method
    # rep.when represents the test step and only gets the use case call  the result of the execution is a failure.
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'driver' in item.fixturenames:
                    web_driver = item.funcargs['driver']
                else:
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),  # add screenshot of allure report
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

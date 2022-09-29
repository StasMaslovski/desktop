from abc import ABC
from typing import Tuple
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePageObject(ABC):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fluent_wait = WebDriverWait(
            self.driver, timeout=7, poll_frequency=1, ignored_exceptions=[NoSuchElementException]
        )
        self.locator_sample = (By.XPATH, "")
        self.unique_element_locator = None

    def is_page_open(self):
        try:
            self.fluent_wait.until(ec.presence_of_element_located(self.unique_element_locator))
            return True
        except TimeoutException:
            return False

    def _get_visible_element(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _fill_input(self, locator: Tuple[By, str], value: str):
        self._get_visible_element(locator).send_keys(value)

    def _tap_enter(self, locator: Tuple[By, str]):
        self._get_visible_element(locator).send_keys(Keys.ENTER)

    def _clear_field(self, locator: Tuple[By, str]):
        self._get_visible_element(locator).clear()

    def accept_alert(self):
        self.driver.find_element_by_name('Ok').click()

    def is_element_with_text_present_on_the_screen(self, text):
        try:
            self._get_visible_element((By.NAME, f"{text}"))
            return True
        except TimeoutException:
            return False

from page_objects.base_page import BasePageObject
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import By


class TranslateText(BasePageObject):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.text_translate_field_locator = (By.NAME, "Type text here")
        self.swap_languages_button_locator = (By.XPATH, "//*[text()='Swap languages']")


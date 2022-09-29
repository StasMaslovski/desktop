from page_objects.base_page import BasePageObject
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy


class TranslateText(BasePageObject):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.text_translate_field_locator = (MobileBy.NAME, "Type text here")
        self.text_translate_field_locator = (MobileBy.ACCESSIBILITY_ID, "wordInput")
        self.swap_languages_button_locator = (MobileBy.XPATH, "//*[text()='Swap languages']")
        # self.rephrase_tab_button_locator = ()

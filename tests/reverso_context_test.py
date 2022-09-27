import pytest
import allure
from page_objects.translate_text_page import TranslateText


@pytest.mark.parametrize(
    "russian_word, english_word",
    [
        ("hello", "привет"),
        ("world", "мир "),
        ("python", "питон")
    ]
)
def test_translate_from_rus_to_eng(driver, russian_word, english_word):
    translate_text_page = TranslateText(driver)
    with allure.step(f"Input {russian_word} in the text field"):
        translate_text_page._fill_input(translate_text_page.text_translate_field_locator, russian_word)
    with allure.step("Taping the enter button"):
        translate_text_page._tap_enter(translate_text_page.text_translate_field_locator)
    with allure.step("Clearing the text field"):
        translate_text_page._clear_field(translate_text_page.text_translate_field_locator)
    with allure.step(f"Check if {english_word} present on the screen"):
        assert translate_text_page.is_element_with_text_present_on_the_screen(english_word)

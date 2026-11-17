import allure
import pytest

from pages.the_internet.iframe_page import IFramePage

pytestmark = pytest.mark.the_internet


@allure.feature("Frames")
def test_type_text_inside_iframe_editor(driver):
    page = IFramePage(driver)
    page.open_page()
    page.type_in_editor("typed from selenium")

    assert page.get_editor_text() == "typed from selenium"

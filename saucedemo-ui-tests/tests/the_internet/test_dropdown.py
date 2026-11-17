import allure
import pytest

from pages.the_internet.dropdown_page import DropdownPage

pytestmark = pytest.mark.the_internet


@allure.feature("Dropdown")
@pytest.mark.parametrize("option", ["Option 1", "Option 2"])
def test_select_dropdown_option(driver, option):
    page = DropdownPage(driver)
    page.open_page()
    page.choose(option)

    assert page.get_selected() == option

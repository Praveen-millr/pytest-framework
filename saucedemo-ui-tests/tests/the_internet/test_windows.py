import allure
import pytest

from pages.the_internet.windows_page import WindowsPage

pytestmark = pytest.mark.the_internet


@allure.feature("Windows")
def test_new_window_opens_and_main_window_is_still_available(driver):
    page = WindowsPage(driver)
    page.open_page()
    main_window = page.get_current_window()

    page.open_new_window()
    page.switch_to_new_window(main_window)
    assert page.get_heading() == "New Window"

    page.close_window_and_switch_to(main_window)
    assert page.get_heading() == "Opening a new window"

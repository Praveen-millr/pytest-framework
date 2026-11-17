import allure
import pytest

from pages.the_internet.dynamic_loading_page import DynamicLoadingPage

pytestmark = pytest.mark.the_internet


@allure.feature("Waits")
@pytest.mark.parametrize(
    "example",
    [1, 2],
    ids=["element_hidden_in_dom", "element_added_to_dom"],
)
def test_result_text_appears_after_loading(driver, example):
    page = DynamicLoadingPage(driver)
    page.open_example(example)
    page.start()

    assert page.get_result() == "Hello World!"

import allure
import pytest

from pages.the_internet.alerts_page import AlertsPage

pytestmark = pytest.mark.the_internet


@pytest.fixture
def alerts_page(driver):
    page = AlertsPage(driver)
    page.open_page()
    return page


@allure.feature("JavaScript alerts")
class TestAlerts:

    def test_accept_simple_alert(self, alerts_page):
        alerts_page.trigger_alert()
        assert alerts_page.accept_alert() == "I am a JS Alert"
        assert alerts_page.get_result() == "You successfully clicked an alert"

    def test_accept_confirm(self, alerts_page):
        alerts_page.trigger_confirm()
        alerts_page.accept_alert()
        assert alerts_page.get_result() == "You clicked: Ok"

    def test_dismiss_confirm(self, alerts_page):
        alerts_page.trigger_confirm()
        alerts_page.dismiss_alert()
        assert alerts_page.get_result() == "You clicked: Cancel"

    def test_answer_prompt(self, alerts_page):
        alerts_page.trigger_prompt()
        alerts_page.answer_prompt("selenium")
        assert alerts_page.get_result() == "You entered: selenium"

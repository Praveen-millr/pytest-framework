import allure
import pytest

from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.login_page import LoginPage
from utils.data_reader import load_json

USERS = load_json("users.json")


@allure.feature("Login")
class TestLogin:

    @pytest.mark.smoke
    @allure.title("Valid user can log in")
    def test_valid_user_can_log_in(self, driver, login_page):
        user = USERS["valid_user"]
        login_page.login(user["username"], user["password"])

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded()
        assert inventory_page.get_title() == "Products"

    @pytest.mark.regression
    @pytest.mark.parametrize("case", USERS["invalid_logins"], ids=lambda case: case["id"])
    def test_invalid_login_shows_error(self, login_page, case):
        login_page.login(case["username"], case["password"])
        assert case["error"] in login_page.get_error_message()

    @pytest.mark.smoke
    @allure.title("Logged in user can log out")
    def test_logout(self, driver, inventory_page):
        inventory_page.logout()
        assert LoginPage(driver).is_loaded()

import allure
import pytest

from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_complete_page import CheckoutCompletePage
from pages.saucedemo.checkout_info_page import CheckoutInfoPage
from pages.saucedemo.checkout_overview_page import CheckoutOverviewPage
from utils.data_reader import load_json

CHECKOUT_DATA = load_json("checkout.json")


@pytest.fixture
def checkout_info_page(driver, inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    CartPage(driver).click_checkout()
    return CheckoutInfoPage(driver)


@allure.feature("Checkout")
class TestCheckout:

    @pytest.mark.smoke
    @allure.title("User can place an order end to end")
    def test_complete_checkout_flow(self, driver, checkout_info_page):
        customer = CHECKOUT_DATA["valid_customer"]
        checkout_info_page.fill_details(
            customer["first_name"], customer["last_name"], customer["postal_code"]
        )

        overview_page = CheckoutOverviewPage(driver)
        assert overview_page.get_item_names() == ["Sauce Labs Backpack"]
        assert "29.99" in overview_page.get_subtotal()
        overview_page.finish()

        assert CheckoutCompletePage(driver).get_confirmation() == "Thank you for your order!"

    @pytest.mark.regression
    @pytest.mark.parametrize("case", CHECKOUT_DATA["missing_fields"], ids=lambda case: case["id"])
    def test_missing_checkout_field_shows_error(self, checkout_info_page, case):
        checkout_info_page.fill_details(case["first_name"], case["last_name"], case["postal_code"])
        assert case["error"] in checkout_info_page.get_error_message()

import allure
import pytest

from pages.saucedemo.cart_page import CartPage


@allure.feature("Cart")
class TestCart:

    @pytest.mark.smoke
    def test_added_products_appear_in_cart(self, driver, inventory_page):
        products = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for product in products:
            inventory_page.add_to_cart(product)
        inventory_page.open_cart()

        assert sorted(CartPage(driver).get_item_names()) == sorted(products)

    @pytest.mark.regression
    def test_remove_last_product_empties_cart(self, driver, inventory_page):
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.remove_item("Sauce Labs Backpack")
        assert cart_page.is_empty()

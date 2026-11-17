import allure
import pytest


@allure.feature("Inventory")
class TestInventory:

    @pytest.mark.smoke
    def test_six_products_are_listed(self, inventory_page):
        assert len(inventory_page.get_product_names()) == 6

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "option, reverse",
        [("lohi", False), ("hilo", True)],
        ids=["price_low_to_high", "price_high_to_low"],
    )
    def test_sort_by_price(self, inventory_page, option, reverse):
        inventory_page.sort_by(option)
        prices = inventory_page.get_product_prices()
        assert prices == sorted(prices, reverse=reverse)

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "option, reverse",
        [("az", False), ("za", True)],
        ids=["name_a_to_z", "name_z_to_a"],
    )
    def test_sort_by_name(self, inventory_page, option, reverse):
        inventory_page.sort_by(option)
        names = inventory_page.get_product_names()
        assert names == sorted(names, reverse=reverse)

    @pytest.mark.regression
    def test_cart_badge_follows_add_and_remove(self, inventory_page):
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bike Light")
        assert inventory_page.get_cart_count() == 2

        inventory_page.remove_from_cart("Sauce Labs Backpack")
        assert inventory_page.get_cart_count() == 1

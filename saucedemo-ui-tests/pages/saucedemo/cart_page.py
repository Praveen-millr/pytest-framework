import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.helpers import to_slug


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_item_names(self):
        return self.get_texts(self.ITEM_NAMES)

    @allure.step("Remove '{product_name}' from the cart page")
    def remove_item(self, product_name):
        self.click((By.ID, f"remove-{to_slug(product_name)}"))

    def is_empty(self):
        return self.wait_until_invisible(self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.helpers import to_slug


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        return self.is_visible(self.PAGE_TITLE)

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_names(self):
        return self.get_texts(self.PRODUCT_NAMES)

    def get_product_prices(self):
        return [float(price.replace("$", "")) for price in self.get_texts(self.PRODUCT_PRICES)]

    @allure.step("Sort products by '{option}'")
    def sort_by(self, option):
        self.select_by_value(self.SORT_DROPDOWN, option)

    @allure.step("Add '{product_name}' to cart")
    def add_to_cart(self, product_name):
        self.click((By.ID, f"add-to-cart-{to_slug(product_name)}"))

    @allure.step("Remove '{product_name}' from cart")
    def remove_from_cart(self, product_name):
        self.click((By.ID, f"remove-{to_slug(product_name)}"))

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(self.CART_LINK)

    @allure.step("Log out")
    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

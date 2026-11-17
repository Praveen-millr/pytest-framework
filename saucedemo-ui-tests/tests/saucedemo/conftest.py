import pytest

from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.login_page import LoginPage
from utils.data_reader import load_json


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_page()
    return page


@pytest.fixture
def inventory_page(driver, login_page):
    user = load_json("users.json")["valid_user"]
    login_page.login(user["username"], user["password"])
    return InventoryPage(driver)

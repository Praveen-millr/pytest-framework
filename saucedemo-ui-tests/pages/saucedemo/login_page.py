import allure
from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = settings.SAUCEDEMO_URL

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_page(self):
        self.open(self.URL)

    def is_loaded(self):
        return self.is_visible(self.LOGIN_BUTTON)

    @allure.step("Log in as '{username}'")
    def login(self, username, password):
        self.log.info("Logging in as '%s'", username)
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password, mask=True)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

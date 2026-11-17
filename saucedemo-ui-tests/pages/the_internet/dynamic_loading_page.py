from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    RESULT_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def open_example(self, number):
        self.open(f"{settings.THE_INTERNET_URL}/dynamic_loading/{number}")

    def start(self):
        self.click(self.START_BUTTON)

    def get_result(self):
        return self.get_text(self.RESULT_TEXT)

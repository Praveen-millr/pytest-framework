from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def open_page(self):
        self.open(f"{settings.THE_INTERNET_URL}/dropdown")

    def choose(self, option_text):
        self.select_by_visible_text(self.DROPDOWN, option_text)

    def get_selected(self):
        return self.get_selected_option(self.DROPDOWN)

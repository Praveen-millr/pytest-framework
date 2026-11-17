from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class WindowsPage(BasePage):
    NEW_WINDOW_LINK = (By.LINK_TEXT, "Click Here")
    HEADING = (By.TAG_NAME, "h3")

    def open_page(self):
        self.open(f"{settings.THE_INTERNET_URL}/windows")

    def open_new_window(self):
        self.click(self.NEW_WINDOW_LINK)

    def get_heading(self):
        return self.get_text(self.HEADING)

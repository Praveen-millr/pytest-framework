from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class IFramePage(BasePage):
    EDITOR_FRAME = (By.ID, "mce_0_ifr")
    EDITOR_BODY = (By.ID, "tinymce")

    def open_page(self):
        self.open(f"{settings.THE_INTERNET_URL}/iframe")

    def type_in_editor(self, text):
        self.switch_to_frame(self.EDITOR_FRAME)
        editor = self.find(self.EDITOR_BODY)
        editor.clear()
        editor.send_keys(text)
        self.switch_to_default_content()

    def get_editor_text(self):
        self.switch_to_frame(self.EDITOR_FRAME)
        text = self.get_text(self.EDITOR_BODY)
        self.switch_to_default_content()
        return text

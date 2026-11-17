from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")

    def get_confirmation(self):
        return self.get_text(self.CONFIRMATION_HEADER)

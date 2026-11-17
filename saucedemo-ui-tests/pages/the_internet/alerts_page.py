from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class AlertsPage(BasePage):
    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")

    def open_page(self):
        self.open(f"{settings.THE_INTERNET_URL}/javascript_alerts")

    def trigger_alert(self):
        self.click(self.JS_ALERT_BUTTON)

    def trigger_confirm(self):
        self.click(self.JS_CONFIRM_BUTTON)

    def trigger_prompt(self):
        self.click(self.JS_PROMPT_BUTTON)

    def get_result(self):
        return self.get_text(self.RESULT)

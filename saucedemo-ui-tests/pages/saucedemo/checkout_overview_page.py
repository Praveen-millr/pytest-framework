from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    FINISH_BUTTON = (By.ID, "finish")

    def get_item_names(self):
        return self.get_texts(self.ITEM_NAMES)

    def get_subtotal(self):
        return self.get_text(self.SUBTOTAL_LABEL)

    def finish(self):
        self.click(self.FINISH_BUTTON)

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config import settings
from utils.logger import get_logger


class BasePage:
    """Common actions shared by every page object. All waits are explicit."""

    def __init__(self, driver, timeout=settings.EXPLICIT_WAIT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger(self.__class__.__name__)

    def _wait_for(self, condition, locator, description):
        try:
            return self.wait.until(condition(locator))
        except TimeoutException:
            self.log.error("Timed out waiting for element to be %s: %s", description, locator)
            raise

    @allure.step("Open URL {url}")
    def open(self, url):
        self.log.info("Opening %s", url)
        self.driver.get(url)

    def find(self, locator):
        return self._wait_for(EC.visibility_of_element_located, locator, "visible")

    def find_all(self, locator):
        return self._wait_for(EC.visibility_of_all_elements_located, locator, "visible")

    @allure.step("Click {locator}")
    def click(self, locator):
        self.log.info("Clicking %s", locator)
        self._wait_for(EC.element_to_be_clickable, locator, "clickable").click()

    @allure.step("Type into {locator}")
    def type_text(self, locator, text, mask=False):
        shown = "*" * len(text) if mask else text
        self.log.info("Typing '%s' into %s", shown, locator)
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        text = self.find(locator).text
        self.log.info("Text of %s: '%s'", locator, text)
        return text

    def get_texts(self, locator):
        return [element.text for element in self.find_all(locator)]

    def count(self, locator):
        return len(self.driver.find_elements(*locator))

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_until_invisible(self, locator):
        return self._wait_for(EC.invisibility_of_element_located, locator, "invisible")

    def select_by_value(self, locator, value):
        self.log.info("Selecting value '%s' in %s", value, locator)
        Select(self.find(locator)).select_by_value(value)

    def select_by_visible_text(self, locator, text):
        self.log.info("Selecting '%s' in %s", text, locator)
        Select(self.find(locator)).select_by_visible_text(text)

    def get_selected_option(self, locator):
        return Select(self.find(locator)).first_selected_option.text

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_current_url(self):
        return self.driver.current_url

    # iframes
    def switch_to_frame(self, locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # alerts
    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        self.log.info("Accepting alert: '%s'", text)
        alert.accept()
        return text

    def dismiss_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        self.log.info("Dismissing alert: '%s'", alert.text)
        alert.dismiss()

    def answer_prompt(self, text):
        alert = self.wait.until(EC.alert_is_present())
        self.log.info("Answering prompt with '%s'", text)
        alert.send_keys(text)
        alert.accept()

    # windows
    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, original_handle):
        self.wait.until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                return

    def close_window_and_switch_to(self, handle):
        self.driver.close()
        self.driver.switch_to.window(handle)

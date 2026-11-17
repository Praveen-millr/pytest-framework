from datetime import datetime
from pathlib import Path

import allure
import pytest

from config import settings
from utils.driver_factory import create_driver
from utils.logger import get_logger

SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"
log = get_logger("conftest")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=settings.BROWSER,
        choices=("chrome", "firefox", "edge"),
        help="browser to run the tests on",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=settings.HEADLESS,
        help="run the browser without a window",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    log.info("Starting %s (headless=%s)", browser, headless)
    browser_driver = create_driver(browser, headless)
    yield browser_driver

    log.info("Closing browser")
    browser_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser_driver = item.funcargs.get("driver")
    if browser_driver is None:
        return

    SCREENSHOT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{item.name}_{timestamp}.png".replace("/", "_").replace("[", "_").replace("]", "")
    browser_driver.save_screenshot(str(SCREENSHOT_DIR / file_name))
    log.error("Test failed, screenshot saved: %s", file_name)

    allure.attach(
        browser_driver.get_screenshot_as_png(),
        name="screenshot on failure",
        attachment_type=allure.attachment_type.PNG,
    )
    allure.attach(
        browser_driver.current_url,
        name="url at failure",
        attachment_type=allure.attachment_type.TEXT,
    )

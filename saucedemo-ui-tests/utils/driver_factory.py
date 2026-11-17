from selenium import webdriver


def create_driver(browser="chrome", headless=False):
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        _apply_chromium_options(options, headless)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        return webdriver.Chrome(options=options)

    if browser == "edge":
        options = webdriver.EdgeOptions()
        _apply_chromium_options(options, headless)
        return webdriver.Edge(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
        return driver

    raise ValueError(f"Unsupported browser: {browser}")


def _apply_chromium_options(options, headless):
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

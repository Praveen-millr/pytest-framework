import os

SAUCEDEMO_URL = os.getenv("SAUCEDEMO_URL", "https://www.saucedemo.com")
THE_INTERNET_URL = os.getenv("THE_INTERNET_URL", "https://the-internet.herokuapp.com")

BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))

# SauceDemo UI Test Automation

UI test framework built with Selenium WebDriver, Python and pytest, using the Page Object Model.
The main suite runs against [SauceDemo](https://www.saucedemo.com). A smaller set of tests on
[the-internet](https://the-internet.herokuapp.com) covers waits, alerts, iframes, windows and dropdowns.

## Tech stack

- Python 3.10+
- Selenium 4 (Selenium Manager downloads the browser driver automatically)
- pytest, with fixtures, markers and parametrize
- Allure for reporting
- GitHub Actions for CI

## Project structure

```
.
├── config/              settings (URLs, browser, timeouts), overridable with environment variables
├── pages/
│   ├── base_page.py     shared actions with explicit waits and logging
│   ├── saucedemo/       page objects for SauceDemo
│   └── the_internet/    page objects for the-internet
├── tests/
│   ├── saucedemo/       login, inventory, cart and checkout tests
│   └── the_internet/    waits, alerts, iframe, windows, dropdown
├── testdata/            JSON files used by parametrized tests
├── utils/               driver factory, logger, data reader, helpers
├── conftest.py          command line options, driver fixture, screenshot on failure
├── pytest.ini           pytest configuration and markers
└── requirements.txt
```

Locators and page actions live in `pages/`. Tests only call page methods and hold the assertions.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Google Chrome must be installed. Firefox and Edge are supported too.

## Running the tests

```bash
pytest                              # everything
pytest -m smoke                     # quick checks only
pytest -m regression                # wider coverage
pytest -m the_internet              # the-internet scenarios
pytest tests/saucedemo/test_login.py
pytest --browser firefox
pytest --headless
```

Settings can also come from environment variables: `BROWSER`, `HEADLESS`, `EXPLICIT_WAIT`,
`SAUCEDEMO_URL`, `THE_INTERNET_URL`.

## Reports, logs and screenshots

- Logs are printed while the tests run and also written to `logs/test_run.log`. Passwords are masked.
- A screenshot is saved to `screenshots/` and attached to the Allure report whenever a test fails.
- Allure results are written to `reports/allure-results`. To view the report
  (needs the [Allure command line](https://allurereport.org/docs/install/) and Java):

```bash
allure serve reports/allure-results
```

## Design notes

- Explicit waits only. There are no `time.sleep` calls and no implicit wait.
- A new browser is started for every test so tests do not depend on each other.
- Test data (users, checkout details, expected error messages) is kept in `testdata/`.

## CI

`.github/workflows/tests.yml` runs the suite headless on every push and pull request, and uploads
the Allure results, screenshots and logs as build artifacts.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',
                     action='store',
                     default='en-gb',
                     help="Choose interface language for tests (for example ru, fr or es).")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be Chrome!")

    yield browser

    browser.quit()


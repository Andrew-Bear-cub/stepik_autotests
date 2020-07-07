import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en-gb',
                     help="Choose interface language for tests (for example ru, fr or es).")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    try:
        options = Options()
        print(options)
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        yield browser
        browser.quit()

    except pytest.UsageError:
        print("parameter --language is not defined, please, choose your language.")


if __name__ == '__main__':
    pass

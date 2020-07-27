from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest
import random
import string


# Вспомогательная функция для генерации уникального почтового адреса
def generate_email():
    return f"{''.join(random.choice(string.ascii_letters) for _ in range(10))}@mail.ru"


@pytest.mark.need_review_custom_scenarios
def test_should_be_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.need_review_custom_scenarios
def test_unsuccessful_registration_not_valid_data(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user('ololomail@ru', '123456789', '987654321')
    page.should_be_unsuccessful_registration_warnings()


@pytest.mark.need_review_custom_scenarios
def test_unsuccessful_registration_weak_password(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user('ololomail@ru', '1erty4', '1erty4')
    page.should_be_password_warnings()


@pytest.mark.need_review_custom_scenarios
def test_unsuccessful_registration_too_common_password(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user('ololomail@ru', '123456789', '123456789')
    page.should_be_password_warnings()


@pytest.mark.need_review_custom_scenarios
def test_successful_registration(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(generate_email(), '123qwer456', '123qwer456')
    page = MainPage(browser, browser.current_url)
    page.should_be_successful_registration_or_login()


@pytest.mark.need_review_custom_scenarios
def test_unsuccessful_login(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.login_user('no_such_user@exist.ru', '123qwerty456')
    page.should_be_unsuccessful_login_warnings()


@pytest.mark.need_review_custom_scenarios
def test_successful_login(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.login_user('olololo113@mail.ru', '123qwerty456')
    page = MainPage(browser, browser.current_url)
    page.should_be_successful_registration_or_login()

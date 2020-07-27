from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link',
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                  marks=pytest.mark.xfail),
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_title_in_alert()
    page.should_be_total_price_in_alert()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_cart()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty()
    basket_page.should_be_empty_message()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(BasePage.generate_email(), '123qwer456', '123qwer456')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_cart()
        # page.solve_quiz_and_get_code()
        page.should_be_product_title_in_alert()
        page.should_be_total_price_in_alert()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_cart()
        page.should_not_be_success_message()

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_in_current_url()

    def should_be_basket_in_current_url(self):
        assert "basket/" in self.browser.current_url, \
            'Текущая страница не явлется корзиной!'

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Корзина не пуста!'

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            'Сообщение о том, что корзина пуста отсутствует!'

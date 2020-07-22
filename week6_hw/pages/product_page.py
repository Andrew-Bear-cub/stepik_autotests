from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_button()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'Нет кнопки добавления в корзину!'

    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_title_in_alert(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        alert_text = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_ALERT).text
        assert alert_text == product_title, 'Не совпадают названия товара на странице и в алерте!'

    def should_be_total_price_in_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_text = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT).text
        assert alert_text == product_price, 'Не совпадает цена товара с ценой в алерте!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_ALERT), \
            "Алерт отображается!"

    def should_disappeared_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_ALERT), \
            "Алерт не исчез!"


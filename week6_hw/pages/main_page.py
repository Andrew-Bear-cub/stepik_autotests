from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_successful_registration_or_login(self):
        assert self.browser.find_element(*MainPageLocators.SUCCESSFUL_TEXT), \
            'Нет сообщения об успешной регстрации'
        assert self.browser.find_element(*MainPageLocators.ACCOUNT_LINK), \
            "Ссылка на аккаунт отсутствует!"
        assert self.browser.find_element(*MainPageLocators.LOGOUT_LINK), \
            "Ссылка на выход из аккаунта отсутствует!"

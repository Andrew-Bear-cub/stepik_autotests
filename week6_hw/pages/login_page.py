from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Not registration page!'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Форма логина отсутствует!'
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
            "Поле 'почта' отсутствует!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Поле 'пароль' отсутствует!"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET), \
            "Ссылка восстановления пароля отсутствует!"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            "Кнопка 'Войти' отсутствует!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Форма регистрации отсутствует!"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            "Поле 'почта' отсутствует!"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), \
            "Поле 'пароль' отсутствует!"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), \
            "Поле 'повторите пароль' отсутствует!"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            "Кнопка 'Зарегистрироваться' отсутствует!"

    def should_be_unsuccessful_registration_warnings(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_ALERT), \
            'Предупреждение об ошибке отсутствует!'
        assert self.is_element_present(*LoginPageLocators.EMAIL_ALERT), \
            'Предупреждение о некорректном и-мейл отсутствует!'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_ALERT), \
            'Предупреждение о проблемах с паролем отсутствует!'

    def should_be_unsuccessful_login_warnings(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_ERROR_ALERT_FIRST), \
            'Предупреждение об ошибке отсутствует!'
        assert self.is_element_present(*LoginPageLocators.LOGIN_ERROR_ALERT_SECOND), \
            'Просьба ввести корректные данные отсутствует!'

    def should_be_password_warnings(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_ALERT), \
            'Предупреждение об ошибке отсутствует!'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_ALERT), \
            'Предупреждение о проблемах с паролем отсутствует!'

    def register_new_user(self, email, password, confirm):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        password_confirm_input.send_keys(confirm)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def login_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()


from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUCCESSFUL_TEXT = (By.XPATH, "//div[@class ='alertinner wicon']")
    ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/accounts/')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(@href, '/accounts/logout')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.XPATH, "//input[@id = 'id_login-username']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@id = 'id_login-password']")
    PASSWORD_RESET = (By.XPATH, "//a[contains(@href, '/password-reset/')]")
    LOGIN_BUTTON = (By.XPATH, "//button[@name = 'login_submit']")
    LOGIN_ERROR_ALERT_FIRST = (By.XPATH, "//form[@id='login_form']/*[1]")
    LOGIN_ERROR_ALERT_SECOND = (By.XPATH, "//form[@id='login_form']/*[2]")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@id = 'id_registration-email']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@id = 'id_registration-password1']")
    REGISTRATION_CONFIRM_PASSWORD = (By.XPATH, "//input[@id = 'id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name = 'registration_submit']")

    ERROR_ALERT = (By.XPATH, "//div[@class = 'alert alert-danger']")
    EMAIL_ALERT = (By.XPATH, "//input[@id='id_registration-email']//following-sibling::span")
    PASSWORD_ALERT = (By.XPATH, "//input[@id='id_registration-password2']//following-sibling::span")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_ADD_ALERT = (By.XPATH, "//div[@id='messages']/*[1]/div/strong")
    BASKET_PRICE_ALERT = (By.XPATH, "//div[@id='messages']/*[3]/div/p/strong")
    PRODUCT_TITLE = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")


class BasketPageLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//p")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import datetime


# Для проверки наличия элемента на странице
def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def test_new_client_registration_is_possible(browser):
    browser.implicitly_wait(5)
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    browser.get(link)

    reg_email = browser.find_element(By.XPATH, "//input[@id = 'id_registration-email']")
    # Достал срезом число милисекунд, должно быть достаточно для вопроизводимости :)
    reg_email.send_keys(f"{str(datetime.datetime.now())[-6:-1]}@mail.ru")

    reg_pswd1 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password1']")
    reg_pswd1.send_keys("123QWer1qw")

    reg_pswd2 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password2']")
    reg_pswd2.send_keys("123QWer1qw")

    reg_button = browser.find_element(By.XPATH, "//button[@name = 'registration_submit']")
    reg_button.click()

    # Такого локатора достаточно?
    assert is_element_present(browser, By.CSS_SELECTOR, ".alert-success"), 'Регистрация не завершена!'



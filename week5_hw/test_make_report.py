from selenium.webdriver.common.by import By
import random
import string


def test_new_client_registration_is_possible(browser):
    browser.implicitly_wait(5)
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    browser.get(link)

    reg_email = browser.find_element(By.XPATH, "//input[@id = 'id_registration-email']")
    # Нагуглил такой вариант генерации случайной строки
    reg_email.send_keys(f"{''.join(random.choice(string.ascii_letters) for _ in range(10))}@mail.ru")

    reg_pswd1 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password1']")
    reg_pswd1.send_keys("123QWer1qw")

    reg_pswd2 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password2']")
    reg_pswd2.send_keys("123QWer1qw")

    reg_button = browser.find_element(By.XPATH, "//button[@name = 'registration_submit']")
    reg_button.click()

    # Переделал локатор чтобы достать текст, добавил в ассерт сравнение текста приветствия
    success_message = browser.find_element(By.XPATH, "//div[@id='messages']/div/div").text
    assert success_message == 'Thanks for registering!', 'Регистрация неуспешна!'

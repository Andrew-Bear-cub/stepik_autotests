from selenium.webdriver.common.by import By


def test_new_client_registration_is_possible(browser):
    browser.implicitly_wait(5)
    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    browser.get(link)

    reg_email = browser.find_element(By.XPATH, "//input[@id = 'id_registration-email']")
    reg_email.send_keys("ololo19@mail.ru")

    reg_pswd1 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password1']")
    reg_pswd1.send_keys("123QWer1qw")

    reg_pswd2 = browser.find_element(By.XPATH, "//input[@id = 'id_registration-password2']")
    reg_pswd2.send_keys("123QWer1qw")

    reg_button = browser.find_element(By.XPATH, "//button[@name = 'registration_submit']")
    reg_button.click()

    assert browser.find_element(By.XPATH, "//div[@class = 'alertinner wicon']"), 'Регистрация не завершена!'

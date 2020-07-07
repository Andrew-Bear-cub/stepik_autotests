from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def test_add_to_basket_button_is_visible(browser):
    wait = WebDriverWait(browser, 5)
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # sleep чтобы увидеть текст
    sleep(3)

    add_to_basket_button = (By.XPATH, "//form[@id = 'add_to_basket_form']/button")
    assert wait.until(EC.visibility_of_element_located(add_to_basket_button)), 'Кнопка "добить в корзину" отсутствует!'


from selenium import webdriver
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:

    driver.get(link)

    button = driver.find_element_by_css_selector('button')
    button.click()

    alert = driver.switch_to.alert
    alert.accept()

    value = int(driver.find_element_by_css_selector('[id="input_value"]').text)
    result = calc(value)

    text_input = driver.find_element_by_css_selector('[id="answer"]')
    text_input.send_keys(result)

    submit = driver.find_element_by_css_selector('button')
    submit.click()

finally:
    sleep(15)
    driver.quit()

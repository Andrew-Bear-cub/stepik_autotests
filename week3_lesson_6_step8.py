from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:

    driver.get(link)
    price = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id = 'price']"), '$100'))
    book = driver.find_element(By.XPATH, "//button[@id = 'book']").click()

    value = int(driver.find_element_by_css_selector('[id="input_value"]').text)
    result = calc(value)

    text_input = driver.find_element_by_css_selector('[id="answer"]')
    text_input.send_keys(result)

    submit = driver.find_element(By.XPATH, "//button[@id = 'solve']")
    submit.click()

finally:
    sleep(10)
    driver.quit()

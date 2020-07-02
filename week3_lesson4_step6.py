from selenium import webdriver
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'

try:

    driver.get(link)
    value = int(driver.find_element_by_css_selector("[id = 'input_value']").text)
    result = calc(value)

    driver.execute_script("window.scrollBy(0, 100);")

    text_input = driver.find_element_by_css_selector("[id = 'answer']")
    text_input.send_keys(result)

    check = driver.find_element_by_css_selector("[id = 'robotCheckbox']")
    check.click()

    radio = driver.find_element_by_css_selector("[id = 'robotsRule']")
    radio.click()

    submit = driver.find_element_by_css_selector('button')
    submit.click()

finally:
    sleep(15)
    driver.quit()

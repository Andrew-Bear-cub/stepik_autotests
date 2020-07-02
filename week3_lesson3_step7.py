from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

link = 'http://suninjuly.github.io/get_attribute.html'

try:

    driver.get(link)
    chest_value = int(driver.find_element_by_xpath('//img').get_attribute('valuex'))
    result = calc(chest_value)

    text_input = driver.find_element_by_xpath('//input[@id="answer"]')
    text_input.send_keys(result)

    check = driver.find_element_by_xpath('//input[@id = "robotCheckbox"]')
    check.click()

    radio = driver.find_element_by_xpath('//input[@id = "robotsRule"]')
    radio.click()

    submit = driver.find_element_by_xpath('//button')
    submit.click()

finally:
    time.sleep(15)
    driver.quit()


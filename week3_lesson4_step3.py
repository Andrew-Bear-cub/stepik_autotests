from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:

    driver.get(link)

    number1 = int(driver.find_element_by_css_selector('[id="num1"]').text)
    number2 = int(driver.find_element_by_css_selector('[id="num2"]').text)
    result = str(number1+number2)

    select = Select(driver.find_element_by_css_selector('[id="dropdown"]'))
    select.select_by_value(result)

    submit = driver.find_element_by_css_selector('button')
    submit.click()

finally:
    sleep(15)
    driver.quit()
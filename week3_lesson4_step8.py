from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'ololo.txt')

try:

    driver.get(link)

    first_name = driver.find_element_by_xpath("//input[@name='firstname']")
    last_name = driver.find_element_by_xpath("//input[@name='lastname']")
    email = driver.find_element_by_xpath("//input[@name='email']")
    upload_file = driver.find_element_by_xpath("//input[@name='file']")
    submit = driver.find_element_by_xpath('//button')

    first_name.send_keys('lol')
    last_name.send_keys('loloev')
    email.send_keys('ololo')
    upload_file.send_keys(file_path)
    submit.click()

finally:
    sleep(15)
    driver.quit()

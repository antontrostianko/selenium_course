import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    sum = 0
    for elem in browser.find_elements(By.CSS_SELECTOR, 'option'):
        sum += int(elem.text)
    browser.find_element(By.ID, 'input_result').send_keys(sum)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(5)
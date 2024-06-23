import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/selenium/5.5/4/1.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    for div in browser.find_elements(By.CLASS_NAME, 'parent'):
        gray = div.find_element(By.CSS_SELECTOR, 'textarea[color=gray]')
        blue = div.find_element(By.CSS_SELECTOR, 'textarea[color=blue]')
        blue.send_keys(gray.text)
        gray.clear()
        div.find_element(By.CSS_SELECTOR, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/scroll/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    sum = 0
    for element in browser.find_elements(By.CLASS_NAME, 'btn'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        sum += int(browser.find_element(By.ID, 'result').text)
    print(sum)
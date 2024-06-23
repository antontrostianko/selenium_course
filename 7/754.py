import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/window_size/1/')
    browser.implicitly_wait(5)

    browser.set_window_size(555 + 16, 555 + 138)

    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)


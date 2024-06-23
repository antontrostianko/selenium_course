import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    time.sleep(5)
    actions = ActionChains(browser)

    end = browser.find_element(By.CSS_SELECTOR, '.draganddrop_end')

    for block in browser.find_elements(By.CSS_SELECTOR, '.draganddrop'):
        actions.drag_and_drop(block, end).perform()
        time.sleep(1)

    print(browser.find_element(By.ID, 'message').text)
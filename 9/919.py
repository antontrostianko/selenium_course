import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(5)
    actions = ActionChains(browser)

    block = browser.find_element(By.ID, 'draggable')

    for box in browser.find_elements(By.CSS_SELECTOR, '.box'):
        actions.drag_and_drop(block, box).perform()
        time.sleep(1)

    print(browser.find_element(By.ID, 'message').text)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')
    time.sleep(3)

    actions = ActionChains(browser)

    blocks = browser.find_elements(By.CLASS_NAME, 'draganddrop')
    ends = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')

    for block, end in zip(blocks, ends):
        actions.drag_and_drop(block, end).perform()
        time.sleep(1)

    print(browser.find_element(By.ID, 'message').text)
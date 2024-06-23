from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')

    draganddrop = browser.find_element(By.ID, "draggable")
    draganddrop_end = browser.find_element(By.ID, "field2")

    ActionChains(browser).drag_and_drop(draganddrop, draganddrop_end).perform()

    div = browser.find_element(By.ID, 'result')
    WebDriverWait(browser, 10).until(lambda _: div.text != '')
    print(div.text)
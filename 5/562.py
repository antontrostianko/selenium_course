from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/selenium/5.5/1/1.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    for field in browser.find_elements(By.CLASS_NAME, 'text-field'):
        field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/selenium/5.5/2/1.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    for field in browser.find_elements(By.CSS_SELECTOR, '.text-field'):
        if field.get_attribute('disabled') is None:
            field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)



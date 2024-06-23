from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    for check in browser.find_elements(By.CSS_SELECTOR, '.check'):
        check.click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    print(browser.find_element(By.ID, 'result').text)
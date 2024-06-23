from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/selenium/5.5/3/1.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    sum = 0
    for div in browser.find_elements(By.CLASS_NAME, 'parent'):
        if div.find_element(By.CSS_SELECTOR, 'input').is_selected():
            sum += int(div.find_element(By.CSS_SELECTOR, 'textarea').text)
    print(sum)
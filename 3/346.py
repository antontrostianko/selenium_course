from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    sum = 0
    for p in browser.find_elements(By.TAG_NAME, 'p'):
        sum += int(p.text)
    print(sum)
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/scroll/2/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    sum = 0
    for div in browser.find_elements(By.CLASS_NAME, 'item'):
        div.find_element(By.CSS_SELECTOR, 'input').click()
        num = div.find_element(By.CSS_SELECTOR, 'span').text
        if num:
            sum += int(num)
    print(sum)
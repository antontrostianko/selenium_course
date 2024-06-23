from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as browser:

    browser.implicitly_wait(5)
    total = 0

    for url in sites:
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, '.checkbox_class').click()
        total += int(browser.find_element(By.ID, 'result').text) ** 0.5

    print(round(total, 9))


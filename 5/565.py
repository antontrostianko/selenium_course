from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/methods/5/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    res = []
    for link in [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]:
        browser.get(link)
        res.append([browser.get_cookies()[0]['expiry'], int(browser.find_element(By.ID, 'result').text)])
    print(max(res, key=lambda a: a[0])[0])
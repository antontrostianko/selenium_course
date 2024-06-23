from selenium import webdriver
import re

URL = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:

    browser.get(URL)
    total = 0

    for cookie in browser.get_cookies():
        if re.match(r'^secret_cookie_\d+', cookie['name']):
            total += int(cookie['value'])

    print(total)
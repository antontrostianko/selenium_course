from selenium import webdriver
import re

URL = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    print(sum([int(c['value']) for c in browser.get_cookies() if re.search(r'_\d*[02468]', c['name'])]))

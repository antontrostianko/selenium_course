import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('2.1_0.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)
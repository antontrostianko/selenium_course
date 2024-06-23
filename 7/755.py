import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:

    browser.get('https://parsinger.ru/window_size/1/')

    for width, height in itertools.product(window_size_x, window_size_y):
        browser.set_window_size(width + 16, height + 138)
        time.sleep(0.5)
        if text := browser.find_element(By.ID, 'result').text:
            print(text)
            break

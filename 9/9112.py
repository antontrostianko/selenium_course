import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-fullscreen")

with webdriver.Chrome(options=chrome_options) as browser:

    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(3)

    actions = ActionChains(browser)

    pieces = browser.find_elements(By.CLASS_NAME, 'piece')
    ranges = browser.find_elements(By.CSS_SELECTOR, '.range > p')

    for piece, p in zip(pieces, ranges):
        actions.drag_and_drop_by_offset(piece, int(p.text.split(':')[1].replace('px', '')), 0).perform()
        time.sleep(1)

    print(browser.find_element(By.ID, 'message').text)
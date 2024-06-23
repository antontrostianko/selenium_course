import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    x = ((12434107696 * 3) * 2) + 1
    select = Select(browser.find_element(By.ID, 'selectId'))
    select.select_by_visible_text(str(x))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(5)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-fullscreen")

with webdriver.Chrome(options=chrome_options) as browser:

    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')
    time.sleep(3)

    sliders = browser.find_elements(By.CSS_SELECTOR, 'input')
    targets = browser.find_elements(By.CSS_SELECTOR, '.target-value')

    for slider, target in zip(sliders, targets):
        browser.execute_script("arguments[0].setAttribute('value', arguments[1]);", slider, target.text)
        browser.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", slider)
        browser.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", slider)

    print(browser.find_element(By.ID, 'message').text)
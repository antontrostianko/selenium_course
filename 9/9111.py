import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-fullscreen")

with webdriver.Chrome(options=chrome_options) as browser:

    browser.get('https://parsinger.ru/selenium/5.10/4/index.html')
    time.sleep(3)

    actions = ActionChains(browser)

    baskets = browser.find_elements(By.CLASS_NAME, 'basket_color')
    d = {basket.value_of_css_property('background-color'): basket for basket in baskets}

    for ball in browser.find_elements(By.CLASS_NAME, 'ball_color'):
        actions.drag_and_drop(ball, d[ball.value_of_css_property('background-color')]).perform()
        time.sleep(1)

    print(browser.find_element(By.CLASS_NAME, 'message').text)
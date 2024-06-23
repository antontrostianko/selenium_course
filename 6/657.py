from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
    browser.implicitly_wait(3)

    div = browser.find_element(By.CSS_SELECTOR, f'#main_container')

    for _ in range(50):
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div)

    for box in div.find_elements(By.CSS_SELECTOR, 'input[type=checkbox]'):
        if not int(box.get_attribute('value')) % 2:
            box.click()

    browser.find_element(By.CSS_SELECTOR, '.alert_button').click()
    print(browser.switch_to.alert.text)

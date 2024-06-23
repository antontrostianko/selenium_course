from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    browser.implicitly_wait(5)

    result = browser.find_element(By.ID, 'result')

    for button in browser.find_elements(By.CSS_SELECTOR, '.buttons'):

        button.click()
        browser.switch_to.alert.accept()

        if result.text:
            break

    print(result.text)



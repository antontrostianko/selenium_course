from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    browser.implicitly_wait(5)

    for button in browser.find_elements(By.CSS_SELECTOR, '.clickMe'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    print(browser.switch_to.alert.text)



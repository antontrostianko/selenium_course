from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    browser.implicitly_wait(5)

    result = browser.find_element(By.ID, 'result')
    input = browser.find_element(By.ID, 'input')
    check = browser.find_element(By.ID, 'check')

    for button in browser.find_elements(By.CSS_SELECTOR, '.buttons'):

        button.click()

        alert_text = browser.switch_to.alert.text
        browser.switch_to.alert.accept()

        input.send_keys(alert_text)
        check.click()

        if result.text != 'Неверный пин-код':
            print(result.text)
            break


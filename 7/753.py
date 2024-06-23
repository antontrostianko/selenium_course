from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    browser.implicitly_wait(5)

    result = browser.find_element(By.ID, 'result')
    check = browser.find_element(By.ID, 'check')

    for pin in browser.find_elements(By.CSS_SELECTOR, '.pin'):

        text = pin.text

        check.click()
        prompt = browser.switch_to.alert

        prompt.send_keys(text)
        prompt.accept()

        if result.text != 'Неверный пин-код':
            print(result.text)
            break

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    browser.implicitly_wait(5)

    for frame in browser.find_elements(By.CSS_SELECTOR, 'iframe'):

        browser.switch_to.frame(frame)
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        num = browser.find_element(By.ID, 'numberDisplay').text

        browser.switch_to.default_content()

        text_field = browser.find_element(By.ID, 'guessInput')

        text_field.send_keys(num)
        browser.find_element(By.ID, 'checkBtn').click()

        try:
            print(browser.switch_to.alert.text)
            break
        except Exception as e:
            text_field.clear()



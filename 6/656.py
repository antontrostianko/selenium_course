from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    actions = ActionChains(browser)

    for button in browser.find_elements(By.CSS_SELECTOR, 'button'):
        actions.click_and_hold(button).pause(float(button.get_attribute('value'))).release(button).perform()

    print(browser.switch_to.alert.text)

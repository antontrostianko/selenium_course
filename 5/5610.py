from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = 'https://parsinger.ru/selenium/5.5/5/1.html'

with webdriver.Chrome() as browser:

    browser.get(URL)
    browser.implicitly_wait(5)

    for div in browser.find_elements(By.CSS_SELECTOR, '#main-container > div'):

        color = div.find_element(By.CSS_SELECTOR, 'span').text
        Select(div.find_element(By.CSS_SELECTOR, 'select')).select_by_value(color)
        div.find_element(By.CSS_SELECTOR, f"button[data-hex='{color}']").click()
        div.find_element(By.CSS_SELECTOR, 'input[type=checkbox]').click()
        div.find_element(By.CSS_SELECTOR, 'input[type=text]').send_keys(color)
        div.find_element(By.CSS_SELECTOR, 'input + button').click()

    browser.find_element(By.CSS_SELECTOR, 'body > button').click()
    print(browser.switch_to.alert.text)



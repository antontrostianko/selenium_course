from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')

    WebDriverWait(browser, 10).until(EC.element_located_to_be_selected((By.ID, 'myCheckbox')))

    browser.find_element(By.CSS_SELECTOR, 'button').click()

    print(browser.find_element(By.ID, 'result').text)




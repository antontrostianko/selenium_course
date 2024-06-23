from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()

    print(WebDriverWait(browser, 5).until(EC.alert_is_present()).text)
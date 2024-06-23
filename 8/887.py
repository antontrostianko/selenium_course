from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    keys = []

    for button in browser.find_elements(By.CSS_SELECTOR, '.box_button'):
        button.click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'close_ad'))).click()
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
        WebDriverWait(browser, 10).until(lambda _: button.text != '')
        keys.append(button.text)


    print('-'.join(filter(None, keys)))


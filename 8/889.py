from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import concurrent.futures

def task(browser, div):
    WebDriverWait(browser, 10).until(EC.element_to_be_selected(div.find_element(By.CSS_SELECTOR, 'input')))
    div.find_element(By.CSS_SELECTOR, 'button').click()


with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    containers = browser.find_elements(By.CSS_SELECTOR, '.container')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, browser, div) for div in containers]

    concurrent.futures.wait(futures)

    print(browser.find_element(By.ID, 'result').text)

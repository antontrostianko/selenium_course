from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/blank/3/index.html')
    browser.implicitly_wait(5)

    main_page = browser.current_window_handle

    total = 0

    for button in browser.find_elements(By.CSS_SELECTOR, 'input'):
        button.click()

    for window in browser.window_handles:
        browser.switch_to.window(window)
        total += 0 if not browser.title.isdigit() else int(browser.title)

    print(total)


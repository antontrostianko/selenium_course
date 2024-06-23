from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    action = ActionChains(browser)
    total = 0

    for i in range(1, 6):

        div = browser.find_element(By.CSS_SELECTOR, f'#scroll-container_{i} div')
        scroll_container = browser.find_element(By.ID, f"scroll-container_{i}")

        while True:
            action.move_to_element(div).scroll_by_amount(0, 100).pause(0.1).perform()
            try:
                scroll_container.find_element(By.CSS_SELECTOR, '.last-of-list')
                break
            except Exception as e:
                pass

        for span in scroll_container.find_elements(By.TAG_NAME, 'span'):
            total += int(span.text) if span.text.isdigit() else 0

    print(total)

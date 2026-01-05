from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = None

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = math.log(abs(12 * math.sin(x)))

    # поле для ответа
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))

    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()

finally:
    time.sleep(10)
    if browser is not None:
        browser.quit()
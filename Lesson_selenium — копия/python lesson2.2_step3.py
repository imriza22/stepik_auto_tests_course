from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math
def calc(a, b):
    return a + b

browser = None
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.ID, "num1")
    x_element2 = browser.find_element(By.ID, "num2")
    x1 = int(x_element1.text)
    x2 = int(x_element2.text)
    result = calc(x1, x2)

    result_str = str(result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result_str)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

finally:
    if browser is not None:
        browser.quit()

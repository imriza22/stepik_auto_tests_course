from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = None

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # берём x со страницы
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = math.log(abs(12 * math.sin(x)))

    # поле для ответа
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))

    # находим кнопку и прокручиваем к ней
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # ставим чекбокс и радиобаттон
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # теперь нажимаем кнопку (один раз, в самом конце)
    button.click()

finally:
    time.sleep(30)
    if browser is not None:
        browser.quit()

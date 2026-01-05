from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
book_button = browser.find_element(By.ID, "book")
book_button.click()


x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
result = math.log(abs(12 * math.sin(x)))

# поле для ответа
answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(str(result))

solve_button = browser.find_element(By.ID, "solve")
solve_button.click()

time.sleep(10)
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = None

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Firuza")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Askerova")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    if not os.path.exists(file_path):
        open(file_path, "w").close()

    element = browser.find_element(By.ID, "file")# добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    if browser is not None:
        browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Создаем экземпляр WebDriver
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Функция для выполнения задания
try:
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")
    for _ in range(3):
        # Используем WebDriverWait для ожидания появления кнопки
        blue_button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(concat(' ', normalize-space(@class),' '), 'btn-primary')]")))
        blue_button.click()
        blue_button = WebDriverWait(firefox, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(concat(' ', normalize-space(@class),' '), 'btn-primary')]")))
        blue_button.click()
        sleep(5)
        chrome.switch_to.alert.accept()
        firefox.switch_to.alert.accept()

# Закрываем браузер
finally:
    chrome.quit()
    firefox.quit()

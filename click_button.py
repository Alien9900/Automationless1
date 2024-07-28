from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указываем путь к WebDriver
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


try:
    # Открываем страницу
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Находим кнопку "Add Element" и кликаем на нее пять раз
    for _ in range(5):
        add_button = chrome.find_element(By.XPATH, "//button[text()='Add Element']").click()

        add_button = firefox.find_element(By.XPATH, "//button[text()='Add Element']").click()
        time.sleep(1)  # небольшая задержка для наглядности

    # Собираем список кнопок "Delete"
    firefox_delete_buttons = chrome.find_elements(By.XPATH, "//button[text()='Delete']")
    chrome_delete_buttons = firefox.find_elements(By.XPATH, "//button[text()='Delete']")

    # Выводим на экран размер списка
    print(f"Количество кнопок 'Delete': {len(chrome_delete_buttons)}")
    print(f"Количество кнопок 'Delete': {len(firefox_delete_buttons)}")

finally:
    # Закрываем браузер после небольшой задержки
    time.sleep(5)  # Задержка для наглядности
    chrome.quit()
    firefox.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указываем путь к WebDriver
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Находим кнопку "Add Element" и кликаем на нее пять раз
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        time.sleep(1)  # небольшая задержка для наглядности

    # Собираем список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Add Element']")

    # Выводим на экран размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрываем браузер после небольшой задержки
    time.sleep(5)  # Задержка для наглядности
    driver.quit()

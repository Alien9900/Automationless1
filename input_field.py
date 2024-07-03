from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Создаем экземпляр WebDriver
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# Открываем страницу
chrome.get("http://the-internet.herokuapp.com/inputs")


# Находим поле ввода и вводим текст "1000"
input_field = chrome.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")

# Ждем немного для наглядности
time.sleep(2)

# Очищаем поле ввода
input_field.clear()

# Ждем немного для наглядности
time.sleep(2)

# Вводим текст "999" в очищенное поле
input_field.send_keys("999")

# Ждем немного для наглядности
time.sleep(2)

# Закрываем браузер
chrome.quit()


firefox.get("http://the-internet.herokuapp.com/inputs")

input_field = firefox.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")

# Ждем немного для наглядности
time.sleep(2)

# Очищаем поле ввода
input_field.clear()

# Ждем немного для наглядности
time.sleep(2)

# Вводим текст "999" в очищенное поле
input_field.send_keys("999")

# Ждем немного для наглядности
time.sleep(2)

# Закрываем браузер
firefox.quit()
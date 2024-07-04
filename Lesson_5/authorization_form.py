from selenium import webdriver
from selenium.webdriver.common.by import By
import time



chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username_field = chrome.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password_field = chrome.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
login_button = chrome.find_element(By.TAG_NAME, "button")
login_button.click()

time.sleep(2)

chrome.quit()

firefox.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username_field = firefox.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password_field = firefox.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
login_button = firefox.find_element(By.TAG_NAME, "button")
login_button.click()

time.sleep(2)

firefox.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password_field = driver.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

time.sleep(2)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# Ввод текста в поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
submit_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
submit_button.click()

# Получение текста кнопки
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# Вывод текста кнопки в консоль
print(button_text)

# Закрытие браузера
driver.quit()

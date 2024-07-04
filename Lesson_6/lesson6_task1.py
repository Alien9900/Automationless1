from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()

# Получение текста из зеленой плашки
text_to_print = driver.find_element(By.CSS_SELECTOR, "#content").text

# Вывод текста в консоль
print(f"Data loaded with AJAX get request: {text_to_print}")

driver.quit()

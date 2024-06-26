from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера (выберите нужный браузер)
driver = webdriver.Chrome()  # Используйте Chrome, Firefox или другой браузер

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ждем, пока модальное окно не появится
    wait = WebDriverWait(driver, 5)
    close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "modal-footer")))
    sleep(2)

    # Кликаем на кнопку "Close"
    close_button.click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    # Закрываем браузер после выполнения скрипта
    driver.quit()

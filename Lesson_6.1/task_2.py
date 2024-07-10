import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    driver.get(URL_2)
    
    # Вводим значение 45 в поле #delay
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Нажимаем на кнопки 7, +, 8, =
    buttons = ["7", "+", "8", "="]
    
    for button in buttons:
        driver.find_element(By.XPATH, f"//span[text()='{button}']").click()
    
    # Ждем появления результата
    result = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    result_text = driver.find_element(By.CLASS_NAME, "screen").text
    
    # Проверяем результат
    assert result_text == "15"

if __name__ == "__main__":
    pytest.main()

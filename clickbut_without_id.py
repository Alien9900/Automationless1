from selenium import webdriver
from time import sleep


# Создаем экземпляр WebDriver
driver = webdriver.Chrome()

# Функция для выполнения задания
try:
        # Открываем страницу
        count = 0
        driver.get("http://uitestingplayground.com/dynamicid")

        # Находим кнопку по атрибуту класса (так как ID динамический, используем класс, который, как предполагается, остается неизменным)
        button = driver.find_element(
              "xpath" , "//button[text()='Button with Dynamic ID']")

        for _ in range(3):
            button = driver.find_element(
                  "xpath" , "//button[text()='Button with Dynamic ID']")
            count = count + 1
            sleep(2)
            print(count)
        

except Exception as ex:
        print(f"Произошла ошибка: {ex}")

# Закрываем браузер
finally:
    driver.quit()


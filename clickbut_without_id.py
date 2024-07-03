from selenium import webdriver
from time import sleep


# Создаем экземпляр WebDriver
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
# Функция для выполнения задания
try:
        # Открываем страницу
        count = 0
        chrome.get("http://uitestingplayground.com/dynamicid")
        firefox.get ("http://uitestingplayground.com/dynamicid")

        # Находим кнопку по атрибуту класса (так как ID динамический, используем класс, который, как предполагается, остается неизменным)
        button = chrome.find_element(
              "xpath" , "//button[text()='Button with Dynamic ID']")
        button = firefox.find_element(
              "xpath" , "//button[text()='Button with Dynamic ID']")

        for _ in range(3):
            button = chrome.find_element(
                  "xpath" , "//button[text()='Button with Dynamic ID']")
            button = firefox.find_element(
                  "xpath" , "//button[text()='Button with Dynamic ID']")
            count = count + 1
            sleep(2)
            print(count)
        

except Exception as ex:
        print(f"Произошла ошибка: {ex}")

# Закрываем браузер
finally:
    chrome.quit()
    firefox.quit()


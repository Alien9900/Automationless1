from selenium.webdriver.common.by import By
from Lesson_7.constants import URL_3

class ShopmainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(URL_3)
#Авторизация на сайте
    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()
#Находим товары
    def buy_issue(self):
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.t_short = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
 #Добавление в корзину       
    def click_issue(self):
        self.browser.find_element(*self.backpack).click()
        self.browser.find_element(*self.t_short).click()
        self.browser.find_element(*self.onesie).click()
#Оформление заказа
    def into_container(self):
        self.Container = (By.ID, "shopping-cart_container")
        self.browser.find_element(*self.Container).click()    
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Локаторы """
FIRST_NAME_REQUIRED = '[placeholder$="name"]'
LAST_NAME_REQUIRED = '[placeholder$="last name"]'
EMAIL_REQUIRED = '[placeholder$="email"]'

class TestAbs(unittest.TestCase):
    def test_1_success(self):

        link = "http://suninjuly.github.io/registration1.html"
        # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # Ввод имени
        first_name_placeholder = browser.find_element(By.CSS_SELECTOR, FIRST_NAME_REQUIRED)
        first_name_placeholder.send_keys("Ivan")

        # Ввод фамилии (выдает ошибку "NoSuchElementException", т.к. такое поле удалили)
        last_name_placeholder = browser.find_element(By.CSS_SELECTOR, LAST_NAME_REQUIRED)
        last_name_placeholder.send_keys("Petrov")

        # Выше тест падает и данные строки уже не выполняются, оставновленные ошибкой выше
        email_placeholder = browser.find_element(By.CSS_SELECTOR, EMAIL_REQUIRED)
        email_placeholder.send_keys("some.email@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не прошла успешно")
        # assert "Congratulations! You have successfully registered!" == welcome_text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_2_fail(self):

        link = "http://suninjuly.github.io/registration2.html"
        # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # Ввод имени
        first_name_placeholder = browser.find_element(By.CSS_SELECTOR, FIRST_NAME_REQUIRED)
        first_name_placeholder.send_keys("Ivan")

        # Ввод фамилии (выдает ошибку "NoSuchElementException", т.к. такое поле удалили)
        last_name_placeholder = browser.find_element(By.CSS_SELECTOR, LAST_NAME_REQUIRED)
        last_name_placeholder.send_keys("Petrov")

        # Выше тест падает и данные строки уже не выполняются, оставновленные ошибкой выше
        email_placeholder = browser.find_element(By.CSS_SELECTOR, EMAIL_REQUIRED)
        email_placeholder.send_keys("some.email@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Регистрация не прошла успешно")
        # assert "Congratulations! You have successfully registered!" == welcome_text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()

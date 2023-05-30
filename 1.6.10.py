from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Локаторы """
FIRST_NAME_REQUIRED = '[placeholder$="name"]'
LAST_NAME_REQUIRED = '[placeholder$="last name"]'
EMAIL_REQUIRED = '[placeholder$="email"]'

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_placeholder = browser.find_element(By.CSS_SELECTOR, FIRST_NAME_REQUIRED)
    first_name_placeholder.send_keys("Ivan")

    last_name_placeholder = browser.find_element(By.CSS_SELECTOR, LAST_NAME_REQUIRED)
    last_name_placeholder.send_keys("Petrov")

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
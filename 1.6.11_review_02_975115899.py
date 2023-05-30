from selenium import webdriver
import time
from selenium.webdriver.common.by import By

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys('тест')

    last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys('тест')

    email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    email.send_keys("тест")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
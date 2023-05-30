import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_link_text"

# Селекторы
print(str(math.ceil(math.pow(math.pi, math.e)*10000))) #проверка математического значения
link_selector = str(math.ceil(math.pow(math.pi, math.e)*10000))
value1 = 'input'
value2 = 'last_name'
value3 = 'city'

try:
    # Открытие ссылки
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    # Осуществляется подмена переменной "link" на локальное значение
    link = browser.find_element(By.LINK_TEXT, link_selector)
    link.click()

    # Заполнение формы
    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # Клик по кнопке "Отправить"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 6 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

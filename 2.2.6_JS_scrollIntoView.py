# https://stepik.org/lesson/228249/step/5?unit=200781

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Визуальный дебагинг """
from scripts.js_execute_script import JSExecuteScript


""" Локаторы """
INPUT = '#answer'  # Таких локатора 2, но выбирается первый, нам подходит
ROBOT_CHECKBOX = '#robotCheckbox'
ROBOT_RULES_RADIO = '#robotsRule'
PEOPLE_RULES_RADIO = '#peopleRule'
VALUE_OF_X = '#input_value'
SUBMIT_BUTTON = 'button[type="submit"]'

""" Ссылки """
link = "http://suninjuly.github.io/execute_script.html"

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)


    # Считывание значения "X"
    x_element = browser.find_element(By.CSS_SELECTOR, VALUE_OF_X)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, x_element)


    # Скрол до инпута
    input_element = browser.find_element(By.CSS_SELECTOR, INPUT)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, input_element)
    # Скрол до элемента по селектору
    browser.execute_script(JSExecuteScript.SCROLL_TO_ELEMENT_TOP_OF_SCREEN, input_element)


    # Вычисление формулы
    # Перевод в текст
    x = x_element.text
    def calc(x):
        """ Вычисление формулы """
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y, ' = y')


    # Вписывание значения формулы в инпут
    input_element = browser.find_element(By.CSS_SELECTOR, INPUT)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, input_element)
    input_element.send_keys(y)

    # Отметить чекбокс "Я робот"
    robot_checkbox_element = browser.find_element(By.CSS_SELECTOR, ROBOT_CHECKBOX)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, robot_checkbox_element)
    click_robot_checkbox_element = robot_checkbox_element.click()


    # Клик по радио "Роботы рулят"
    robot_radio = browser.find_element(By.CSS_SELECTOR, ROBOT_RULES_RADIO)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, robot_radio)
    robot_radio_click = robot_radio.click()

    # Клик по кнопке "Сабмит"
    submit_button = browser.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, submit_button)
    click_submit_button = submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

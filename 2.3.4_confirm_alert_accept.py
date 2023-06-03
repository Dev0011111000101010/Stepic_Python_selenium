# https://stepik.org/lesson/184253/step/4?unit=158843

import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Визуальный дебагинг """
from scripts.js_execute_script import JSExecuteScript


""" Ссылки """
link = 'http://suninjuly.github.io/alert_accept.html'

""" Локаторы """
# XPATH
XPATH_BUTTON_I_WANT_TO_GO_ON_A_MAGIC_JOURNEY = '//button[text()="I want to go on a magical journey!"]'
XPATH_SUBMIT_BUTTON = '//button[text()="Submit"]'
# CSS
CSS_VALUE_OF_X = '#input_value'
CSS_INPUT_DATA = '#answer'

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    """ Клик по кнопке """
    button_element = browser.find_element(By.XPATH, XPATH_BUTTON_I_WANT_TO_GO_ON_A_MAGIC_JOURNEY)
    button_element_click = button_element.click()

    """ Принятие confirm алерта """
    confirm = browser.switch_to.alert
    confirm.accept()

    """ Поиск значения 'X' и перевод его в текст """
    value_of_x_element = browser.find_element(By.CSS_SELECTOR, CSS_VALUE_OF_X)
    convert_vlue_of_x_to_text = value_of_x_element.text
    x = convert_vlue_of_x_to_text

    """ Вычисление формулы """
    def calc(x):
        print(x, ' = x = распечатка изнутри функции "def calc(x)"')
        """ Вычисление формулы """
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y, ' = y')

    """ Инпут полученных данны """
    input_element = browser.find_element(By.CSS_SELECTOR, CSS_INPUT_DATA)
    input_element.send_keys(y)

    """ Клик по кнопке сабмит """
    submit_button = browser.find_element(By.XPATH, XPATH_SUBMIT_BUTTON)
    submit_button_click = submit_button.click()

    """ Вывод цифр результата в консоль IDE = можно убрать 'вэйт' из 'finally' """
    print(browser.switch_to.alert.text, " = Вывод цифр результата в консоль IDE = можно убрать 'вэйт' из 'finaly'")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
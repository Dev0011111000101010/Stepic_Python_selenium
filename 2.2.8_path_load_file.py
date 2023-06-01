# https://stepik.org/lesson/228249/step/8?unit=200781

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
link = "http://suninjuly.github.io/file_input.html"

""" Локаторы """
INPUT_FIRST_NAME = '[placeholder="Enter first name"]'
INPUT_LAST_NAME = '[placeholder="Enter last name"]'
INPUT_EMAIL = '[placeholder="Enter email"]'
UPLOAD_FILE_BUTTON = '#file'
SUBMIT_BUTTON = '[type="Submit"]'

""" Данные """
input_name = "Имя"
input_last_name = "Фамилия"
input_email = "some@email.com"

""" Дебагинг """
# Путь + имя файла
print(os.path.abspath(__file__), ' = os.path.abspath(__file__)')
# Путь (только)
print(os.path.abspath(os.path.dirname(__file__)), ' = os.path.abspath(os.path.dirname(__file__))')

""" Путь к файлу """
# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir, ' = current_dir')
# Дополнительная вложенная папке где лежит файл
additional_dir_name = 'files'
# Название файла
file_name = 'f.txt'
# Добавляем название файла и слеш между путем и файлом
absolute_path_and_slash_and_filename = os.path.join(current_dir, additional_dir_name, file_name)
print(absolute_path_and_slash_and_filename, ' = absolute_path_and_filename_and_slash')
# Используем более простую переменную
absolute_path_to_file = absolute_path_and_slash_and_filename

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    """ Данные в первый инпут (имя) """
    input_element_first_name = browser.find_element(By.CSS_SELECTOR, INPUT_FIRST_NAME)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, input_element_first_name)
    input_element_first_name.send_keys(input_name)

    """ Данные во второй инпут (фамилия) """
    input_element_last_name = browser.find_element(By.CSS_SELECTOR, INPUT_LAST_NAME)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, input_element_last_name)
    input_element_last_name.send_keys(input_last_name)

    """ Данные в третий инпут (email) """
    input_element_email = browser.find_element(By.CSS_SELECTOR, INPUT_EMAIL)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, input_element_email)
    input_element_email.send_keys(input_email)

    """ Клик по кнопке добавления файла """
    upload_file_button = browser.find_element(By.CSS_SELECTOR, UPLOAD_FILE_BUTTON)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, upload_file_button)
    # upload_file_button_click = upload_file_button.click()
    upload_file_button_action = upload_file_button.send_keys(absolute_path_to_file)

    """ Клик по кнопке отправки """
    submit_button = browser.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)
    # Покрасить найденный элемент
    browser.execute_script(JSExecuteScript.COLOR_RED_and_BORDER_3PX_SOLID_RED, submit_button)
    # upload_file_button_click = upload_file_button.click()
    submit_button_click = submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

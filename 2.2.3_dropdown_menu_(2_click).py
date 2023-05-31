# https://stepik.org/lesson/228249/step/2?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


""" Локаторы """
DROPDOWN_SELECT_CSS = '#dropdown'
NUMBER_1_CSS = '#num1'
NUMBER_2_CSS = '#num2'
text_of_element_in_dropdown_menu = '' # чтобы не выдавало ошибку
DROPDOWN_RESULT_CSS = f'[value*="{text_of_element_in_dropdown_menu}"]'
SUBMIT_BUTTON_CSS = '[type="submit"]'


""" Ссылки """
link = "http://suninjuly.github.io/selects1.html"

""" JS скрипты"""
# Дебагинг, нужный ли элемент найден
script_colour = "arguments[0].style.setProperty('color', 'red', 'important');"
script_border = "arguments[0].style.setProperty('border', '3px', 'red', 'solid', 'important');"


try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    number_1_element = browser.find_element(By.CSS_SELECTOR, NUMBER_1_CSS)
    browser.execute_script(script_colour, number_1_element)
    browser.execute_script(script_border, number_1_element)
    number_1_text = number_1_element.text
    print(number_1_text, ' = number_1_text')

    number_2_element = browser.find_element(By.CSS_SELECTOR, NUMBER_2_CSS)
    browser.execute_script(script_colour, number_2_element)
    browser.execute_script(script_border, number_2_element)
    number_2_text = number_2_element.text
    print(number_2_text, ' = number_2_text')

    def sum(num1, num2):
        return int(num1) + int(num2)

    text_of_element_in_dropdown_menu = sum(number_1_text, number_2_text)
    print(text_of_element_in_dropdown_menu, " = text_of_element_in_dropdown_menu")

    DROPDOWN_RESULT_CSS = f'[value*="{text_of_element_in_dropdown_menu}"]'
    select_item = browser.find_element(By.CSS_SELECTOR, DROPDOWN_SELECT_CSS)
    browser.execute_script(script_colour, select_item)
    browser.execute_script(script_border, select_item)
    select_item_click = select_item.click()

    select_result = browser.find_element(By.CSS_SELECTOR, DROPDOWN_RESULT_CSS)
    browser.execute_script(script_colour, select_result)
    browser.execute_script(script_border, select_result)
    select_result_click = select_result.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON_CSS)
    browser.execute_script(script_colour, submit_button)
    browser.execute_script(script_border, submit_button)
    submit_button_click = submit_button.click()


    # select_item = Select(browser.find_element(By.CSS_SELECTOR, DROPDOWN_SELECT_CSS)).click()
    # browser.execute_script(script, select_item)
    # click_on_dropdown_result_bypassing_select_item = select_item.select_by_visible_text(text_of_element_in_dropdown_menu).click()
    # browser.execute_script(script, click_on_dropdown_result_bypassing_select_item)


finally:
    # ожидание в секундах, чтобы визуально оценить результаты прохождения скрипта
    time.sleep()
    # закрываем браузер после всех манипуляций
    browser.quit()
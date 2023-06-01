from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Локаторы """
INPUT = '#answer'  # Таких локатора 2, но выбирается первый, нам подходит
ROBOT_CHECKBOX = '#robotCheckbox'
ROBOT_RULES_RADIO = '#robotsRule'
PEOPLE_RULES_RADIO = '#peopleRule'
VALUE_OF_X = '#input_value'
SUBMIT_BUTTON = 'button[type="submit"]'

""" Ссылки """
link = "https://suninjuly.github.io/math.html"

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    robot_radio = browser.find_element(By.CSS_SELECTOR, ROBOT_RULES_RADIO)
    robot_radio_click = robot_radio.click()


    x_element = browser.find_element(By.CSS_SELECTOR, VALUE_OF_X)
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y, ' = y')

    input_element = browser.find_element(By.CSS_SELECTOR, INPUT)
    input_element.send_keys(y)

    click_robot_checkbox_element = browser.find_element(By.CSS_SELECTOR, ROBOT_CHECKBOX).click()
    click_robot_radio_element = browser.find_element(By.CSS_SELECTOR, ROBOT_RULES_RADIO).click()
    click_submit_button = browser.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON).click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
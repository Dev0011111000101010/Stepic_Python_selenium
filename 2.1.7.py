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
TREASURE_IMG = '#treasure'

""" Ссылки """
link = "http://suninjuly.github.io/get_attribute.html"

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    treasure_value = browser.find_element(By.CSS_SELECTOR, TREASURE_IMG)
    hidden_in_treasure_value_of_x = treasure_value.get_attribute('valuex')
    print(hidden_in_treasure_value_of_x, " = hidden_in_treasure_value_of_x")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(hidden_in_treasure_value_of_x)
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
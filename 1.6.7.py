from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

LINK = "http://suninjuly.github.io/huge_form.html"
INPUT_CSS_SELECTOR_100_ITEMS = 'input'

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(LINK)
    elements = browser.find_elements(By.CSS_SELECTOR, INPUT_CSS_SELECTOR_100_ITEMS)
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

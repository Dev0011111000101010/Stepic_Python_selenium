from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/find_xpath_form"

value1 = 'input'
value2 = 'last_name'
value3 = 'city'
BUTTON_XPATH_SELECTOR = '//div[6]/button[3]'


try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, value1)
    # input1 = browser.find_element(By.CSS_SELECTOR, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    # input2 = browser.find_element(By.CSS_SELECTOR, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    # input3 = browser.find_element(By.CSS_SELECTOR, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, BUTTON_XPATH_SELECTOR)
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

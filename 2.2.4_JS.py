# https://stepik.org/lesson/228249/step/4?unit=200781
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" Ссылки """
link = "http://suninjuly.github.io/selects1.html"

try:
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    # ожидание в секундах, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
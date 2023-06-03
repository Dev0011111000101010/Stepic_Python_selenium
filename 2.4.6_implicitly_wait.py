from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
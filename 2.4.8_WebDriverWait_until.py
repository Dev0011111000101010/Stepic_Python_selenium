import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

""" Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


""" Ссылки """
link = 'http://suninjuly.github.io/explicit_wait2.html'

""" Локаторы """
# XPATH
XPATH_BUTTON_BOOK = '//button[text()="Book"]'
XPATH_SUBMIT_BUTTON = '//button[text()="Submit"]'
# CSS
CSS_PRICE = '#price'
CSS_VALUE_OF_X = '#input_value'
CSS_INPUT_DATA = '#answer'

try:
    """ Запуск драйвера """
    # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    """ Дождаться цены дома в 100$ и нажать кнопку 'Book' """
    # Кликабальна цена
    booking_price_is_clickable = WebDriverWait(browser, 20).until(
        EC.all_of(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_PRICE)),
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, CSS_PRICE), '$100')
        )
    )

    # # Попытка написать: ЕСЛИ цена = 100$, ТО кликать кнопку
    # wait_until_price_100 = WebDriverWait(browser, 5).until(
    #     browser.find_element(By.CSS_SELECTOR, CSS_PRICE).text == '$100'
    # )


    # booking_price_is_100 =
    booking_button_element = browser.find_element(By.XPATH, XPATH_BUTTON_BOOK)
    booking_button_element_click = booking_button_element.click()


    # Ожидание правильной цены в $100
    # booking_price_text = booking_price.text
    # print(booking_price_text, ' = print(booking_price) (ДО функции)')
    # while booking_price_text !== '$100':
    #     print(booking_price_text, ' = print(booking_price) (ВНУТРИ функции)')
    #     booking_button_element = browser.find_element(By.XPATH, XPATH_BUTTON_BOOK)
    #     booking_button_element_click = booking_button_element.click()
    # print(booking_price_text, ' = print(booking_price) (ПОСЛЕ функции)')

    """ Ожидание, пока появится математическая задача """
    wait_for_clicable_value_of_x_element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_VALUE_OF_X)))

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
    # закрываем браузер после всех манипуляций
    browser.quit()

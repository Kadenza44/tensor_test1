from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class YandexSearchPage:
    URL = 'https://yandex.ru'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def find_element_id(self, text):
        try:
            search_input = self.browser.find_element(By.ID, text)
        except NoSuchElementException:
            print(f"Элемент с id = '{text}' не найден на странице")
        else:
            return search_input

    def check_element_class_name(self, class_name):
        time = 10
        try:
            elem = WebDriverWait(self.browser, time).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        except TimeoutException:
            print(f"Элемент с именем класса = '{class_name}' не отобразился на странице за время {time} секунд")
        else:
            return elem


    def input_text(self, web_element_input, phrase):
        web_element_input.send_keys(phrase)


    def press_return(self, web_element):
        web_element.send_keys(Keys.RETURN)

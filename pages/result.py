from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class YandexResultSearchPage:

    def __init__(self, browser):
        self.browser = browser

    def check_result_search(self):
        try:
            elem = self.browser.find_element(By.ID, 'search-result')
        except NoSuchElementException:
            print(f"Элемент с id = 'search-result' не найден на странице (нет результатов поиска)")
        else:
            return elem

    def list_result_search(self, count_iter, check_text):
        count = 0
        for i in range(1, count_iter + 1, 1):
            link = self.browser.find_element(By.XPATH, f'//*[@id="search-result"]/li[{i}]')
            if check_text in link.text:
                count += 1
        return count

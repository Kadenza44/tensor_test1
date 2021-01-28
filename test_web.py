from selenium.webdriver import Chrome, Firefox
import pytest

from pages.search import YandexSearchPage
from pages.result import YandexResultSearchPage

BROWSER = Chrome()  # браузер для теста
PHRASE = 'тензор'  # фраза для проверки
LINK_AMOUNT_CHECK = 1  # Сколько первых ссылок в результатах поиска должны содержать CHECK_LINK
CHECK_LINK = 'tensor.ru'  # Проверяемая ссылка в результатах поиска

# надстройки при обращении к драйверу браузера
@pytest.fixture
def browser():
    driver = BROWSER
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_r(browser):
    search_page = YandexSearchPage(browser)
    search_page.load()
    web_element = search_page.find_element_id('text')
    assert web_element, 'Нет поисковой строки'
    search_page.input_text(web_element, PHRASE)
    element_suggest = search_page.check_element_class_name('mini-suggest__popup_visible')
    assert element_suggest, 'Нет окна suggest с подсказками'
    search_page.press_return(web_element)

    result_search = YandexResultSearchPage(browser)
    resutl = result_search.check_result_search()
    assert resutl, 'Нет результатов поиска'
    amount_link = result_search.list_result_search(LINK_AMOUNT_CHECK, CHECK_LINK)
    assert amount_link == LINK_AMOUNT_CHECK, f'Только в {amount_link} первых результатах поиска есть {CHECK_LINK}'


# test_r(Chrome())
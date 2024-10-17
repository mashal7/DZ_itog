from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Base:
    '''Базовый класс, содержит универсальные методы'''

    def __init__(self, driver):
         self._driver = driver

    def get_current_url(self):
        '''Метод для возврата url'''

        get_url = self._driver.current_url
        print(f'Текущий url: {get_url}')

    def assert_word(self, word, expect_result):
        '''Метод для проверки надписи'''

        value_word = word.text
        print(value_word)
        assert value_word == expect_result, 'Ошибка! Надпись неверна'
        print('Надпись верна. Проверка пройдена успешно')

    def assert_url(self, expect_url):
        '''Метод для проверки url'''

        get_url = self._driver.current_url
        assert get_url == expect_url, 'Ошибка! Url неверный'
        print('Url верный. Проверка пройдена успешно')


    def go_to_main_page(self):
        '''Метод для возврата на главную страницу'''

        main_page = '//div[@class="header__column header__column--logo"]'
        wait = WebDriverWait(self._driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH, main_page))).click()

    def wait_load_widget(self):
        '''Метод для загрузги виджеты (для проверки url)'''

        # полный url доступен только после полной загрузки страницы (виджет снизу справа последний грузится)
        widget = '//div[@class="b24-widget-button-inner-container"]'
        wait = WebDriverWait(self._driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH, widget)))





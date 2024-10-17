import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class BooksPage(Base):
    """ Класс, содержащий локаторы и методы для страницы Книги"""

    def __init__(self, driver):
        super().__init__(driver)

    # ----------------------------Locators----------------------------
    books_button = '(//a[@href="/catalog/knigi/"])[4]'      # кнопка книги

    # ----------------------------Getters----------------------------
    @property
    def types_of_books(self):
        '''Геттеры всех типов книг'''
        descriptions = self._driver.find_elements(by=By.CLASS_NAME, value='accordionHead__toggle ')
        books_types = {desc.text: desc for desc in  descriptions}
        return books_types

    @property
    def get_books_button(self):
        # кнопка книги
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.books_button)))

    # ----------------------------Actions----------------------------
    def click_books_button(self):
        self.get_books_button.click()
        print('Переход в каталог книг')

    # ----------------------------Methods----------------------------

    def select_type_book(self, type):
        '''Выбор типа книг: всего 4 типа'''
        self.click_books_button()
        self.get_current_url()
        types_book = self.types_of_books
        # проверка на существование определенного типа
        try:
            types_book[type].click()
            print(f'Переход в каталог "{type}"')
        except KeyError:
            print('Такого выбора в каталоге нет')
        except Exception as err:
            print(f'Произошла ошибка: {err}')





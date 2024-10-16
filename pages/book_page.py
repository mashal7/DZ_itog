import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class BooksPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    books_button = '(//a[@href="/catalog/knigi/"])[4]'

    @property
    def types_of_books(self):
        books_types = {}
        descriptions = self._driver.find_elements(by=By.CLASS_NAME, value='accordionHead__toggle ')
        for desc in descriptions:
            print(desc)
            #books_types[desc.text] = desc
        return books_types


    #Getters
    @property
    def get_books_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.books_button)))


    # Actions
    def click_books_button(self):
        self.get_books_button.click()
        print('Переход в каталог: {}')

    # Methods
    # выбор типа литературы
    def select_type_book(self, type='Художественная литература'):
        print('Выбор типа литературы')
        self.click_books_button()
        print(self.types_of_books)
        #self.click_type_book(self.types_of_books['Художественная литература'])




import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class FictionPage(Base):
    """ Класс содержащий локаторы и методы для страницы книги, подтип - Художественная литература"""

    def __init__(self, driver):
        super().__init__(driver)

    # ----------------------------Locators----------------------------
    locators_types_fiction = [f'//a[@data-id="{i}"]' for i in range(2885, 2898)]        # жанры художественной литературы
    field_author = '//input[@name="filter[576]"]/following-sibling::input[@placeholder="Поиск..."]'
    author_boccaccio = '//div[@data-ga-label="Боккаччо Д."]'
    book_binding = '//div[@data-ga-label="Твердая обложка"]'
    button_apply_filter = '//button[@class="btn btn--primary btn--fullWidth"]'
    button_add_to_cart = '//a[@class="btn btn--border50 js-add-to-cart"]'
    check_author = '//div[@class="card__subtitle hiddenMobile"]'
    check_price = '//div[@class="price price--ruble"]'

    # ----------------------------Getters----------------------------
    @property
    def types_of_fiction_books(self):
        wait = WebDriverWait(self._driver, 10)
        d = {}
        for locator in self.locators_types_fiction:
            type = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            d[type.text.rsplit(' ', 1)[0]] = type
        return d

    @property
    def get_field_author(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.field_author)))

    @property
    def get_specific_author(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.author_boccaccio)))

    @property
    def get_book_binding(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.book_binding)))

    @property
    def get_button_apply_filter(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filter)))

    @property
    def get_button_add_to_cart(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    @property
    def get_check_author(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.check_author)))

    @property
    def get_check_price(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.check_price)))


    #---------------------------------Actions----------------------------------------------
    def input_author(self, author):
        self.get_field_author.send_keys(author)
        print(f'Пишем в фильтре автора {author}')

    def click_specific_author(self):
        self.get_specific_author.click()
        print('Выбираем фильтр с нужным автором')

    def click_book_binding(self):
        self.get_book_binding.click()
        print('Выбираем фильтр, где переплетом книги является "Твердая обложка"')

    def click_button_apply_filter(self):
        self.get_button_apply_filter.click()
        print('Подтверждаем фильтр')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart.click()
        print('Кладем книгу в корзину')


    # -----------------------------Methods---------------------------
    # выбор типа литературы
    def select_type_fiction(self, type):
        self.get_current_url()
        types_book = self.types_of_fiction_books

        try:
            types_book[type].click()
            print(f'Переход в каталог "{type}"')
        except KeyError:
            print('Такого выбора в каталоге нет')
        except Exception as err:
            print(f'Произошла ошибка: {err}')

    # Настройка фильтра
    def set_up_filter_author_binding(self, author):
        print(f'Установка фильтра книг с автором {author} и твёрдой обложкой')
        self.input_author(author)
        self.click_specific_author()
        self.click_book_binding()
        self.click_button_apply_filter()

        self.wait_load_widget()
        self.get_current_url()
        self.assert_url('https://fkniga.ru/catalog/klassicheskaja-proza/?filter%5B576%5D=43228&filter%5B578%5D=40368')
        print('Фильтр применен успешно')

    def add_book_to_cart(self):
        self.click_button_add_to_cart()
        print('Книга в корзине')

    @property
    def autor_price_for_checking(self):
        return self.get_check_author.text, self.get_check_price.text




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
    locators_types_fiction = [f'//a[@data-id="{i}"]' for i in range(2885, 2898)]      # жанры художественной литературы
    field_author = '//input[@name="filter[576]"]/following-sibling::input[@placeholder="Поиск..."]'     # поле для поиска автора
    author_boccaccio = '//div[@data-ga-label="Боккаччо Д."]'                          # выбор автора: Боккаччо (можно будет настроить универсальный локатор)
    book_binding = '//div[@data-ga-label="Твердая обложка"]'                          # выбор переплета Твердая обложка
    button_apply_filter = '//button[@class="btn btn--primary btn--fullWidth"]'        # кнопка подтверждения фильтра
    button_add_to_cart = '//a[@class="btn btn--border50 js-add-to-cart"]'             # кнопка Положить в корзину
    check_author = '//div[@class="card__subtitle hiddenMobile"]'                      # надпись автор для проверки
    check_price = '//div[@class="price price--ruble"]'                                # надпись цена для проверки

    # ----------------------------Getters----------------------------
    @property
    def types_of_fiction_books(self):
        '''Геттеры всех жанров художественной литературы'''
        wait = WebDriverWait(self._driver, 10)
        d = {}
        for locator in self.locators_types_fiction:
            type = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            d[type.text.rsplit(' ', 1)[0]] = type
        return d

    @property
    def get_field_author(self):
        # поле для поиска автора
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.field_author)))

    @property
    def get_specific_author(self):
        # выбор определенного автора (в данном случае Бокаччо)
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.author_boccaccio)))

    @property
    def get_book_binding(self):
        # выбор переплета Твердая обложка
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.book_binding)))

    @property
    def get_button_apply_filter(self):
        # кнопка подтверждения фильтра
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_apply_filter)))

    @property
    def get_button_add_to_cart(self):
        # кнопка Положить в корзину
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    @property
    def get_check_author(self):
        # надпись автор для проверки
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.check_author)))

    @property
    def get_check_price(self):
        # надпись автор для цены
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.check_price)))


    #---------------------------------Actions----------------------------------------------
    def input_author(self, author):
        self.get_field_author.send_keys(author)
        print(f'Пишем в фильтре автора: {author}')

    def click_specific_author(self):
        self.get_specific_author.click()
        print('Выбираем галочку с нужным автором в фильтре')

    def click_book_binding(self):
        self.get_book_binding.click()
        print('Выбираем фильтр, где переплетом книги является "Твердая обложка"')

    def click_button_apply_filter(self):
        self.get_button_apply_filter.click()
        print('Применяем фильтры')

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart.click()
        print('Кладем книгу в корзину')


    # -----------------------------Methods---------------------------
    # выбор жанра художественной литературы
    def select_type_fiction(self, type):
        '''Выбор жанра "Художественная литература, переход и проверка"'''
        self.get_current_url()
        types_book = self.types_of_fiction_books

        # проверка на существование определенного жанра
        try:
            types_book[type].click()
            print(f'Переход в каталог "{type}"')
        except KeyError:
            print('Такого выбора в каталоге нет')
        except Exception as err:
            print(f'Произошла ошибка: {err}')

    # Настройка фильтров
    def set_up_filter_author_binding(self, author):
        '''Настройка фильра: автор "Бокаччо, твердый переплёт"'''

        print(f'Установка фильтра книг с автором {author} и твёрдой обложкой')
        self.input_author(author)
        self.click_specific_author()
        self.click_book_binding()
        self.click_button_apply_filter()

        #self.wait_load_widget()  - если есть виджет
        time.sleep(7)
        self.get_current_url()
        self.assert_url('https://fkniga.ru/catalog/klassicheskaja-proza/?filter%5B576%5D=43228&filter%5B578%5D=40368')
        print('Фильтр применен успешно')

    def add_book_to_cart(self):
        '''Положить книгу в корзину'''

        self.click_button_add_to_cart()
        print('Книга в корзине')

    @property
    def autor_price_for_checking(self):
        '''Получение данных о книге (автор, цена) для дальнейших проверок'''

        return self.get_check_author.text, self.get_check_price.text




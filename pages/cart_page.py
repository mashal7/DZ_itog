import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.fiction_page import FictionPage


class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        super().__init__(driver)

    # ----------------------------------Locators----------------------------------

    button_cart = '//a[@href="/cart/"]'                                             # кнопка Корзина
    price = '//span[@class="price price--sm price--ruble cartBoxList__price"]'      # цена книги для сверки
    author = '//p["data-v-6c0c2814"]'                                               # автор книги для сверки
    button_place_order = '//a[@class="btn btn--primary btn--fullWidth btn-next-loading cartBox__button-dekstop"]'   # кнопка для оформления заказа

    # -----------------------------Getters----------------------------------------
    @property
    def get_button_cart(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    @property
    def get_author(self):
        # автор книги для сверки
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.author)))

    @property
    def get_price(self):
        # цена книги для сверки
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.price)))

    @property
    def get_button_place_order(self):
        # кнопка для оформления заказа
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.button_place_order)))

    #Actions
    def click_button_cart(self):
        self.get_button_cart.click()
        print(f'Нажинаем на "Корзина"')

    def click_button_place_order(self):
        self.get_button_place_order.click()
        print('Нажинаем на "Перейти к оформлению"')


    # ----------------------------Methods----------------------------------

    def check_author_price(self, expect_author, expect_price):
        '''Вход в корзину и сверка автора и цены в корзине и каталоге, проверка url'''

        # переходим в корзину, сверяем url
        self.click_button_cart()
        self.get_current_url()
        self.assert_url('https://fkniga.ru/cart/')

        print('Сверяем автора и цену в каталоге и корзине')
        expect_author = expect_author.split(' ', 1)[1]
        self.assert_word(self.get_author, expect_author)
        self.assert_word(self.get_price, expect_price)
        print('Автор и цена указаны верно')

        # переходим в оформление заказа, проверяем url
        self.click_button_place_order()
        #self.wait_load_widget()  - если есть виджет
        time.sleep(7)
        self.get_current_url()
        self.assert_url('https://fkniga.ru/cart/order/')
        self.get_screenshot()
        print('Страница оформления заказа верна')




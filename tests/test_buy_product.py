import pytest

from pages.book_page import BooksPage
from pages.cart_page import CartPage
from pages.fiction_page import FictionPage
from pages.login_page import LoginPage


def test_buy_product(driver):
    """Тест по покупке товара включает в себя:
    авторизацию, переход в каталог книг, художественную литературу
    выбор товара по фильтру автор - Бокаччо, тверый переплет

    При повторном тесте освободить корзину перед началом теста"""

    # авторизация
    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(driver)
    authorization.log_in(mail, password)

    # переход в каталог книг, тип 'Художественная литература'
    books = BooksPage(driver)
    books.select_type_book('Художественная литература')

    # выбор жанра 'Классическая литература', фильтрация
    fiction = FictionPage(driver)
    fiction.select_type_fiction('Классическая литература')
    fiction.set_up_filter_author_binding('Боккаччо')
    fiction.add_book_to_cart()

    # переход в корзину,оформление заказа
    cart = CartPage(driver)
    expect_author, expect_price = fiction.autor_price_for_checking
    cart.check_author_price(expect_author, expect_price)

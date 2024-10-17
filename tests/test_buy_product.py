import pytest

from pages.book_page import BooksPage
from pages.cart_page import CartPage
from pages.fiction_page import FictionPage
from pages.login_page import LoginPage


def test_buy_product(set_up):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(set_up)
    authorization.log_in(mail, password)

    books = BooksPage(set_up)
    books.select_type_book('Художественная литература')

    fiction = FictionPage(set_up)
    fiction.select_type_fiction('Классическая литература')
    fiction.set_up_filter_author_binding('Боккаччо')
    fiction.add_book_to_cart()

    cart = CartPage(set_up)
    expect_author, expect_price = fiction.autor_price_for_checking
    cart.check_author_price(expect_author, expect_price)

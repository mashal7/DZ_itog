import pytest

from pages.book_page import BooksPage
from pages.login_page import LoginPage


def test_buy_product(set_up):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(set_up)
    authorization.log_in(mail, password)

    books = BooksPage(set_up)
    books.select_type_book()


import pytest

from pages.login_page import LoginPage


def test_buy_product(set_up):
    """Тест по покупке товара включает в себя:
    авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'werty123'
    authorization = LoginPage(set_up)
    authorization.log_in(mail, password)


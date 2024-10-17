import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""
    def __init__(self, driver):
        super().__init__(driver)

    # ----------------------------Locators----------------------------
    log_in_button = '//a[@class="btn btn--controlMain btn-auth"]'   # кнопка авторизации
    mail = '//input[@name="phone_or_email"]'                        # ввод почты
    password = '//input[@name="password"]'                          # ввод пароля
    enter_button = '//button[@class="btn btn--primary btn--height60 btn--fullWidth"]'   # кнопка входа
    word_to_check_log_in ='//h1[@class="main__title title title--48"]'          # слово для проверки авторизации


    # ----------------------------Getters----------------------------
    @property
    def get_log_in_button(self):
        # кнопка авторизации
        wait = WebDriverWait(self._driver, 60)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.log_in_button)))

    @property
    def get_mail(self):
        # ввод почты
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    @property
    def get_password(self):
        # ввод пароля
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    @property
    def get_enter_button(self):
        # кнопка входа
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    @property
    def get_word_to_check_log_in(self):
        # слово для проверки авторизации
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.word_to_check_log_in)))

    # ----------------------------Actions----------------------------
    def click_log_in_button(self):
        self.get_log_in_button.click()
        print('Переход в окно авторизации')

    def input_mail(self, mail):
        self.get_mail.send_keys(mail)
        print('Ввод mail')

    def input_password(self, password):
        self.get_password.send_keys(password)
        print('Ввод пароля')

    def click_enter_button(self):
        self.get_enter_button.click()
        print('Вход в личный кабинет')


    # ----------------------------Methods----------------------------
    # авторизация в системе
    def log_in(self, mail, password):

        print('Авторизация')
        self.get_current_url()
        self.click_log_in_button()
        self.input_mail(mail)
        self.input_password(password)
        self.click_enter_button()

        # проверка
        print('Проверка авторизации')
        self.assert_word(self.get_word_to_check_log_in, 'Личный кабинет')
        print('Авторизация успешно пройдена')

        self.go_to_main_page()




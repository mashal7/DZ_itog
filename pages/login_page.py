import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    log_in_button = '//a[@class="tabs-button"]'
    log_in_password_button = '//button[@class="_button_uzf15_1 _is-large_uzf15_100 _is-white-violet_uzf15_258 _is-border_uzf15_266 nowrap _is-expanded_uzf15_210"]'
    mail = '//input[@id="email"]'
    password = '//input[@id="pass"]'
    enter_button = '//button[@class="_button_uzf15_1 _is-large_uzf15_100 _is-basic_uzf15_190 nowrap _is-expanded_uzf15_210"]'
    word_to_check_log_in = '//div[@class="user-desc__status"]'

    # Getters
    @property
    def get_log_in_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.log_in_button)))

    @property
    def get_log_in_password_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.log_in_password_button)))

    @property
    def get_mail(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    @property
    def get_password(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    @property
    def get_enter_button(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    @property
    def get_word_to_check_log_in(self):
        wait = WebDriverWait(self._driver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, self.word_to_check_log_in)))

    # Actions
    def click_log_in_button(self):
        self.get_log_in_button.click()
        print('Переход в окно авторизации')

    def click_log_in_password_button(self):
        self.get_log_in_password_button.click()
        print('Переход на авторизацию через пароль')

    def input_mail(self, mail):
        self.get_mail.send_keys(mail)
        print('Ввод mail')

    def input_password(self, password):
        self.get_password.send_keys(password)
        print('Ввод пароля')

    def click_enter_button(self):
        self.get_enter_button.click()
        print('Вход в личный кабинет')


    # Methods
    # авторизация в системе
    def log_in(self, mail, password):

        print('Авторизация')
        self.get_current_url()
        self.click_log_in_button()
        self.click_log_in_password_button()
        self.input_mail(mail)
        self.input_password(password)
        self.click_enter_button()
        time.sleep(3)

        # проверка
        # try:
        #     self.click_log_in_button()
        #     self.click_log_in_password_button()
        #     raise AssertionError('Ошибка авторизации')
        # except:
        #     print('Авторизация прошла успешно')

        #self.assert_word(self.get_word_to_check_log_in, 'Покупатель')

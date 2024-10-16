import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up():
    print('Enter browser')
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    url = 'https://my-shop.ru/'
    driver.get(url)
    yield driver
    driver.quit()
    print('Close browser')
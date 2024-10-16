import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up():
    print('Enter browser')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()

    #options.binary_location = "C:\\Users\\\mpetrova\\AppData\\Local\\Programs\\Opera\\opera.exe"
    #service = Service("C:\\Users\\mpetrova\\Desktop\\Less\\chromedriver-win64\\chromedriver.exe")

    # options.binary_location = "C:\\Users\\\masha\\AppData\\Local\\Programs\\Opera\\opera.exe"
    # service = Service(
    #     "C:\\Users\\masha\\OneDrive\\Рабочий стол\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    # driver = webdriver.Chrome(options=options, service=service)

    url = 'https://fkniga.ru/'
    driver.get(url)
    yield driver
    #driver.quit()
    print('Close browser')
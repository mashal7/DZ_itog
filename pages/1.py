import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


word_to_check_log_in = '//div[@class="user-desc__status"]'
options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

url = 'https://my-shop.ru/'
driver.get(url)

wait = WebDriverWait(driver, 10)
a = wait.until(EC.presence_of_element_located((By.XPATH, word_to_check_log_in)))
print(a.text)
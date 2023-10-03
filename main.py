from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://merchant.hepsiburada.com/v2/login?returnUrl=%2F')


try:
    # Kullanıcı adı alanını bulana kadar 10 saniye bekleyecek
    username = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    username.send_keys('tekinhasan73@hotmail.com')

    password = WebDriverWait(driver,timeout=30).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password.send_keys("Hasan5324847381_T")
    driver.find_element(By.ID, 'merchant-sign-in-button').click()
except Exception as e:
    print(f'Hata: {e}')


'''
username = driver.find_element(By.ID,'username')
password = driver.find_element(By.ID,'password')
username.send_keys('tekinhasan73@hotmail.com')
password.send_keys('Hasan5324847381_T')




'''
driver.get('https://merchant.hepsiburada.com/v2/login?returnUrl=%2F')
html = driver.page_source

#soup = BeautifulSoup(html, 'html.parser')

while True:
    continue
# Tarayıcıyı kapatma
driver.quit()

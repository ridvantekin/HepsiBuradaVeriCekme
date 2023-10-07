from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def WebIslemleri():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://merchant.hepsiburada.com/v2/login?returnUrl=%2F')


    try:
        username = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        username.send_keys('tekinhasan73@hotmail.com')

        password = WebDriverWait(driver,timeout=30).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        password.send_keys("Hasan5324847381_T")
        time.sleep(2)
        driver.find_element(By.ID, 'merchant-sign-in-button').click()
        time.sleep(10)
    except Exception as e: #print yerine arayüz mesajı tasarlanacak
        print(f'Hata: {e}')


    try:
        driver.get("https://merchant.hepsiburada.com/finance/records")
        time.sleep(10)
    except Exception as e: #print yerine arayüz mesajı tasarlanacak
        print(f'Hata: {e}')


    selectorAdres = "#root > div > div.layout > div > div.record-page > div > div:nth-child(3) > div.ant-table-wrapper.data-grid > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.ant-table-cell.fixed-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > a > svg"
    try:
        global i
        for i in range(1, 16):
            degistirilmisIdegeri = selectorAdres[169:170]
            degistirilmisIdegeri = i
            selectorAdres = f"#root > div > div.layout > div > div.record-page > div > div:nth-child(3) > div.ant-table-wrapper.data-grid > div > div > div > div > div > table > tbody > tr:nth-child({degistirilmisIdegeri}) > td.ant-table-cell.fixed-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first > a > svg"

            faturaDetayButonu = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selectorAdres))
                )
            faturaDetayButonu.click()
            time.sleep(5)


            try:
                faturaGörüntüleButonu = WebDriverWait(driver, 8).until(
                    EC.presence_of_element_located((By.XPATH,"// *[ @ id = \"root\"] / div / div[1] / div / div / div / div[1] / div[2] / button[1]"))
                    )
                if faturaGörüntüleButonu:
                    faturaGörüntüleButonu.click()
                    faturaGörüntüleButonu = True
                    time.sleep(2)
                    driver.back()
                    time.sleep(2)
                else:
                    continue

            except Exception as e:
                print(f'Haaata: {e}') #print yerine arayüz mesajı tasarlanacak
                time.sleep(5)
                faturaGörüntüleButonu = False
                driver.back()
                continue



    except Exception as e:
        print(f'Hata: {e}') #print yerine arayüz mesajı tasarlanacak

    while True:
        if i == 15:
            break


    driver.quit()
WebIslemleri()
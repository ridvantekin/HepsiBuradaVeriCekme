import sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import messagebox
import os


def cözümlemeİslemi():

    #dosyaYolu = r"C:\Users\VICTUS\Downloads"
    def sil_dosya(dizin, dosya_Adi):
        dosya_yolu = os.path.join(dizin, dosya_Adi)
        try:
            os.remove(dosya_yolu)
            # bu alanda bir frame üzerine hangi dosyaların silindiği yazılabilir.
        except PermissionError:
            messagebox.showerror(title="HATA", message="DOSYA BULUNAMADI \n SİSTEMSEL HATA!")


    indirilen_dizin = r"C:\Users\VICTUS\Downloads"
    dosyalar = os.listdir(indirilen_dizin)
    pdf_dosyalari = [dosya for dosya in dosyalar if dosya.endswith(".pdf")]

    try:

        for pdf_dosyasi in pdf_dosyalari:
            if "(" in pdf_dosyasi and pdf_dosyasi[-5] == ')' and pdf_dosyasi[-6].isdigit() and pdf_dosyasi[-7] == '(':
                silinecekDosya = pdf_dosyasi
                sil_dosya(indirilen_dizin, silinecekDosya)
        messagebox.showinfo(title="SİSTEM MESAJI", message="FATURA ÇÖZÜMLEME İŞLEMİ BAŞARIYLA TAMAMLANMIŞTIR")

    except:
        messagebox.showinfo(title="SİSTEM MESAJI", message="FATURA ÇÖZÜMLEME İŞLEMİ HATALI")
    finally:
        sys.exit()

#----------------------------------------------------------------------------------------------------------------
def WebIslemleri():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://merchant.hepsiburada.com/v2/login?returnUrl=%2F')


    try:
        username = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
        username.send_keys('kullanıcıadı')

        password = WebDriverWait(driver,timeout=30).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        password.send_keys("şifre")
        time.sleep(2)
        driver.find_element(By.ID, 'merchant-sign-in-button').click()
        time.sleep(5)
    except Exception as e:
        messagebox.showerror(title="HATA",message="GİRİŞ İŞLEMİ YAPILAMADI! \n SİSTEM YÖNETİCİNİZ İLE İLETİŞİME GEÇİNİZ")


    try:
        driver.get("https://merchant.hepsiburada.com/finance/records")
        time.sleep(5)
    except Exception as e: #print yerine arayüz mesajı tasarlanacak
        messagebox.showerror(title="HATA",message="MUHASEBE EKRANI AÇILAMADI! \n SİSTEM YÖNETİCİNİZ İLE İLETİŞİME GEÇİNİZ")


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
            time.sleep(4)


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
                messagebox.showerror(title="HATA",message="FATURA GÖRÜNTÜLE BULUNAMADI")
                time.sleep(3)
                faturaGörüntüleButonu = False
                driver.back()
                continue



    except Exception as e:
        messagebox.showerror(title="HATA",message="FATURA DETAY BUTONU BULUNAMADI! \n SİSTEM YÖNETİCİNİZ İLE İLETİŞİME GEÇİNİZ")

    while True:
        if i == 15:
            messagebox.showinfo(title="SİSTEM MESAJI", message="FATURA İNDİRME İŞLEMİ BAŞARIYLA TAMAMLANMIŞTIR")
            break


    driver.quit()

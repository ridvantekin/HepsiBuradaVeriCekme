import requests
from bs4 import BeautifulSoup

# Giriş bilgileri
url = 'https://merchant.hepsiburada.com/v2/login?returnUrl=%2F'  # Giriş sayfasının URL'si
username = 'tekinhasan73@hotmail.com'
password = 'Hasan5324847381_T'
base_url = 'https://merchant.hepsiburada.com'  # Ana URL

# Giriş yapma işlemi
session = requests.Session()
login_payload = {'username': username, 'password': password}
session.post(url, data=login_payload)

## Muhasebe sayfasına yönlendirme
response = session.get(base_url + '/muhasebe')

# Muhasebe sayfasını işle
soup = BeautifulSoup(response.content, 'html.parser')

# Muhasebe butonunu bulma
muhasebe_butonu = soup.find('a', class_='sub', string='Muhasebe')


# Muhasebe butonu var mı diye kontrol etme
if muhasebe_butonu is not None:
    muhasebe_butonu.click()
    print("Muhasebe butonuna tıklandı.")

    # Kayıtlar ve Faturalar metnini içeren etiketi bulma
    kayitlar_faturalar_etiketi = soup.find('p', class_='des', text='Faaliyetlerinize ait tüm kayıtlar ve faturalar')

    # Eğer etiket bulunduysa devam et
    if kayitlar_faturalar_etiketi is not None:
        kayitlar_faturalar_etiketi.parent.click()  # Ebeveyn etikete tıklama işlemi
        print("Kayıtlar ve Faturalar butonuna tıklandı.")
    else:
        print("Kayıtlar ve Faturalar butonu bulunamadı.")

else:
    print("Muhasebe butonu bulunamadı.")
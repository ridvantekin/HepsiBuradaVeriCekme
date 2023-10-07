import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox


def sifremiUnuttum():
    messagebox.showerror("Hata", "LÜTFEN SİSTEM YÖNETİCİNİZ İLE İLETİŞİME GEÇİNİZ")
def giris_kontrol():

    girilen_kullanici_adi = usernameEntry.get()
    girilen_sifre = passwordEntry.get()

    # Kullanıcı adı ve şifreyi kontrol et
    if girilen_kullanici_adi == "a" and girilen_sifre == "a" and len(girilen_sifre) != 0 and len(girilen_sifre) != 0:
        giris_ekrani.destroy()
        ArayuzEkrani()

    else:
        messagebox.showerror("Hata", "GEÇERSİZ KULLANICI ADI VEYA ŞİFRE")
def ArayuzEkrani():
    ana_pencere = tkinter.Tk()
    ana_pencere.title("HepsiBurada Faturaları İndirme Arayüzü")
    ana_pencere.config(bg="#c6e2ff")

    ekran_genisligi = ana_pencere.winfo_screenwidth()
    ekran_yuksekligi = ana_pencere.winfo_screenheight()

    pencere_genisligi = 650
    pencere_yuksekligi = 600

    x = (ekran_genisligi - pencere_genisligi) // 2
    y = (ekran_yuksekligi - pencere_yuksekligi) // 2

    # Pencerenin konumunu ayarla
    y -=70
    ana_pencere.geometry(f"{pencere_genisligi}x{pencere_yuksekligi}+{x}+{y}")

    global img
    resim = Image.open(r"C:\Users\VICTUS\PycharmProjects\hepsiBuradaFaturalarıCekme\logo.png")
    genislik = 250
    yukseklik = 250
    resim = resim.resize((genislik, yukseklik), Image.BILINEAR)
    img = ImageTk.PhotoImage(resim)
    imgCercevesi = tkinter.Label(image=img, borderwidth=0)
    imgCercevesi.anchor("center")
    imgCercevesi.place(x=15, y=20)

    anaEkranBilgiBtn = tkinter.Button()
    anaEkranBilgiBtn.config(text= "DİKKAT! \n \n FATURALARI İNDİRMEK İÇİN İLK ÖNCE 'FATURALARI \n İNDİR' BUTONUNA BASMANIZ GEREKMEKTEDİR.\n \n \n"
                                  "ARDINDAN BİLGİLENDİRME MESAJI GELDİKTEN \n SONRA 'ÇÖZÜMLE' BUTONUNA BASINIZ.",
                            width=46,
                            height=12,
                            justify="center",
                            font=("Verdicane",10,"bold"),
                            bg="#eee685")
    anaEkranBilgiBtn.place(x=257, y=25)

    anaEkranIndirBtn = tkinter.Button()
    





# -----------------------------------------------------------------------------
def girisPaneli(window):
    ekranGenisligi = window.winfo_screenwidth()
    ekranYuksekligi = window.winfo_screenheight()

    pencere_genisligi = 500
    pencere_yuksekligi = 320

    x = (ekranGenisligi - pencere_genisligi) // 2
    y = (ekranYuksekligi - pencere_yuksekligi) // 2

    # Pencerenin konumunu ayarla
    y -=70
    window.geometry(f"{pencere_genisligi}x{pencere_yuksekligi}+{x}+{y}")
#__________________________________________________________________________________

giris_ekrani = tkinter.Tk()
giris_ekrani.title("GİRİŞ EKRANI")
giris_ekrani.geometry("500x320")
giris_ekrani.config(bg="#eee685")
girisPaneli(giris_ekrani)


frame = tkinter.Frame(giris_ekrani, width=200, height=200)
frame.config(width=400,
             height=250,
             bg="#eee685")
frame.place(x=55, y=30)

# ----------------------------------------------------------------------------
usernameLbl = tkinter.Label(giris_ekrani)
usernameLbl.config(text="KULLANICI ADINIZI GİRİNİZ",
                    bg="#eee68f",
                    fg="black",
                    font=("Times New Roman", 14))
usernameLbl.place(x=120, y=40)

# -----------------------------------------------------------------------------

usernameEntry = tkinter.Entry(giris_ekrani)
usernameEntry.config(width=42,
                     justify="center",
                     font=("Verdicana", 13),
                     bg="white")
usernameEntry.focus()
usernameEntry.place(x=60, y=80)

# -----------------------------------------------------------------------------

sifreLbl = tkinter.Label(giris_ekrani)
sifreLbl.config(text="LÜTFEN ŞİFRENİZİ GİRİNİZ",
                bg="#eee68f",
                fg="black",
                font=("Times New Roman", 14))
sifreLbl.place(x=123, y=120)

# ----------------------------------------------------------------------------

passwordEntry = tkinter.Entry(giris_ekrani)
passwordEntry.config(width=42,
                     justify="center",
                     show="*",
                     font=("Verdicana", 13),
                     bg="white")
passwordEntry.place(x=60, y=160)

# ----------------------------------------------------------------------------

girisBtn = tkinter.Button(giris_ekrani)
girisBtn.config(text="GİRİŞ",
                width=11,
                fg="black",
                height=3,
                font=("Arial", 10, "bold"),
                bg="orange",
                command=giris_kontrol)

girisBtn.place(x=345, y=200)

# ----------------------------------------------------------------------------

sifremiUnuttumBtn = tkinter.Button(giris_ekrani)
sifremiUnuttumBtn.config(text="ŞİFREMİ \n UNUTTUM",
                         width=11,
                         height=3,
                         font=("Arial", 10, "bold"),
                         bg="orange",
                         command=sifremiUnuttum)

sifremiUnuttumBtn.place(x=60, y=200)

#----------------------------------------------------------------------------
#giris_ekrani.mainloop()
tkinter.mainloop()

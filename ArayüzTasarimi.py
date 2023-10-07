import time
import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

def ArayuzEkrani(pencere):

    ekran_genisligi = pencere.winfo_screenwidth()
    ekran_yuksekligi = pencere.winfo_screenheight()

    pencere_genisligi = 750
    pencere_yuksekligi = 700

    x = (ekran_genisligi - pencere_genisligi) // 2
    y = (ekran_yuksekligi - pencere_yuksekligi) // 2

    # Pencerenin konumunu ayarla
    y -=70
    pencere.geometry(f"{pencere_genisligi}x{pencere_yuksekligi}+{x}+{y}")

ana_pencere = tkinter.Tk()
ana_pencere.title("HepsiBurada Faturaları İndirme Arayüzü")
ana_pencere.config(bg="#c6e2ff")
ArayuzEkrani(ana_pencere)

def ImageArayuz():
    global img
    resim = Image.open(r"C:\Users\VICTUS\PycharmProjects\hepsiBuradaFaturalarıCekme\logo.png")
    genislik = 250
    yukseklik = 250
    resim = resim.resize((genislik, yukseklik), Image.BILINEAR)
    img = ImageTk.PhotoImage(resim)
    imgCercevesi = tkinter.Label(image=img, borderwidth=0)
    imgCercevesi.anchor("center")
    imgCercevesi.place(x=15, y=20)
ImageArayuz()

#-----------------------------------------------------------------------------
kullaniciAdi = "banyohastanesi"
sifre = "123456"
#-----------------------------------------------------------------------------
def BasariliUyariEkrani():

    messagebox.showinfo(title="SİSTEM MESAJI", message="GİRİŞ BAŞARILI")
def BasarisizUyariEkrani():
    messagebox.showwarning(title="SİSTEM MESAJI", message="LÜTFEN GİRİŞ BİLGİLERİNİ KONTROL EDİNİZ")
#------------------------------------------------------------------------------

def girisİslemi():

    kullaniciAdGirisi = usernameEntry.get()
    sifreGiris = passwordEntry.get()

    if kullaniciAdGirisi == kullaniciAdi and sifreGiris == sifre:
        BasariliUyariEkrani()

    else:
        BasarisizUyariEkrani()

#------------------------------------------------------------------------------

frame = tkinter.Frame(ImageArayuz(), width=200, height=200)
frame.config(width=400, height=250,
             bg="#eee685")
frame.place(x=335, y=30)

#----------------------------------------------------------------------------
usernameLbl = tkinter.Label()
usernameLbl.config(text= "KULLANICI ADINIZI GİRİNİZ",
                   bg="#eee68f",
                   fg="black",
                   font=("Times New Roman",14))
usernameLbl.place(x= 400, y=40)

#-----------------------------------------------------------------------------

usernameEntry = tkinter.Entry()
usernameEntry.config(width=42,
                     justify="center",
                     font=("Verdicana", 13),
                     bg="white")
usernameEntry.focus()
usernameEntry.place(x=340, y=80)
#command girilecek
#-----------------------------------------------------------------------------

sifreLbl = tkinter.Label()
sifreLbl.config(text="LÜTFEN ŞİFRENİZİ GİRİNİZ",
                   bg= "#eee68f",
                   fg="black",
                   font=("Times New Roman",14))
sifreLbl.place(x=403, y=120)

#----------------------------------------------------------------------------

passwordEntry = tkinter.Entry()
passwordEntry.config(width=42,
                     justify="center",
                     show= "*",
                     font=("Verdicana", 13),
                     bg="white")
passwordEntry.place(x=340, y=160)
#command girilecek

#----------------------------------------------------------------------------

girisBtn = tkinter.Button()
girisBtn.config(text="GİRİŞ",
                   width=11,
                   fg="black",
                   height=3,
                   font=("Arial", 10, "bold"),
                   bg="orange",
                   command=girisİslemi)

girisBtn.place(x=625, y=200)

#----------------------------------------------------------------------------

sifremiUnuttumBtn = tkinter.Button()
sifremiUnuttumBtn.config(text="ŞİFREMİ \n UNUTTUM",
                   width=11,
                   height=3,
                   font=("Arial", 10, "bold"),
                   bg="orange",
                   command="UNUTTUM UYARI EKRANI ")

sifremiUnuttumBtn.place(x=340, y=200)

#---------------------------------------------------------------------------




tkinter.mainloop()

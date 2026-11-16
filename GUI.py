import tkinter as tk
from tokenize import String

from Sipariş_classı import Sipariş

class Ana_ekran:
    def __init__(self ):
        self.ekran = tk.Tk()
        self.ekran.geometry("800x600+450+100")
        self.ekran.title("_ _ _ _    Siapriş ve Üretim Takip Otomasyonu    _ _ _ _" )
        self.orta_font = ("Helvetica bold" , 17)
        self.k_font = ("Helvetica italic" ,  15)
        self.b_font = ("Helvetica bold" , 19)

        # TKİNTER DFEĞİŞKENLERİ TANIMLANIYOR
        self.gln_mlz_hmmd_değ = tk.StringVar()
        self.gln_mlz_türü = tk.StringVar()
        self.gln_mlz_tonaj = tk.StringVar()
        self.iş_alış_tarihi_değ = tk.StringVar()
        self.sorumlu_kişi_değ =  tk.StringVar()
        self.sorumlu_iletişim_değ = tk.StringVar()
        self.iş_durumu_değ = tk.BooleanVar() # True veya False
        # ________________________________________________
        self.gdn_mlz_türü_değ = tk.StringVar()
        self.gdn_mlz_tonaj_değ = tk.StringVar()
        self.iş_teslim_tarihi_değ = tk.StringVar()
        self.karşı_kişi_değ = tk.StringVar()
        self.karşı_sorumlu_iletişim_değ = tk.StringVar()

        # şirket adı yazılyor
        self.firma_adı_label = self.label_oluştur(self.ekran , str(Sipariş.kuruluş_adı) , 0 , 0)
        self.firma_adı_label.grid_configure(columnspan=5 , sticky= tk.EW)
        self.firma_adı_label.config( font = self.b_font)

        self.gelen_mazleme_label = self.label_oluştur(self.ekran , "Gelen Malzeme: " , 1 , 0 )
        self.gln_mlz_hmmd_giriş = self.giriş_oluştur(self.ekran , self.gln_mlz_hmmd_değ  , 1 ,1)


    # Label Oluşturan Metod
    def label_oluştur(self ,ekran_adı ,  yazı , satır ,sütun ):
        etiket = tk.Label(ekran_adı , text = yazı , font = self.orta_font )
        etiket.grid(row = satır , column = sütun , padx = 10 , pady = 10)
        return etiket

    # Entry leri oluşturan metod
    def giriş_oluştur(self, ekran , değişken,  satır ,sütun ):
        giriş = tk.Entry(ekran , textvariable= değişken , font = self.k_font )
        giriş.grid(row = satır , column = sütun , padx = 10 , pady = 10)
        değişken.set("    ?")
        return giriş


    def tuş_oluştur(self , ekran , yazı , satır , sütun):
        tuş = tk.Entry(ekran , text = yazı , font = self.orta_font)
        tuş.grid(row = satır , column = sütun , padx = 10 , pady = 10)
        return tuş



    def ekran_döngü(self):
        self.ekran.mainloop()


import tkinter as tk
from tkinter import ttk

from Sipariş_classı import Sipariş

class Ana_ekran:
    def __init__(self ):
        self.ekran = tk.Tk()
        en = self.ekran.winfo_screenwidth()
        boy = self.ekran.winfo_screenheight()

        self.ekran.geometry(f"{en}x{boy}+0+0")

        self.ekran.title("_ _ _ _    Siapriş ve Üretim Takip Otomasyonu    _ _ _ _" )
        self.orta_font = ("Helvetica bold" , 17)
        self.k_font = ("Helvetica italic" ,  15)
        self.b_font = ("Helvetica bold" , 19)
        self.mini_font= ("Helvetica italic" , 13 )

        # TKİNTER DFEĞİŞKENLERİ TANIMLANIYOR
        self.gln_mlz_hmmd_değ = tk.StringVar()
        self.gln_mlz_türü_değ = tk.StringVar()
        self.gln_mlz_tonaj_değ = tk.StringVar()
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

        # combobox listeleri tanımlanıyor
        self.hammade_listesi = ["Bakır" , "Demir" , "Çelik" , "Aluminyum" , "Galvaniz" , "Krom" , "Siyah Demir"]

        # şirket adı yazılyor
        self.firma_adı_label = self.label_oluştur(self.ekran , str(Sipariş.kuruluş_adı) , 0 , 0)
        self.firma_adı_label.grid_configure(columnspan=5 , sticky= tk.EW)
        self.firma_adı_label.config( font = self.b_font)

        # GELEN MALZEME BİLGİLERİ ÇERÇEVESİ TANIMLANIYOR
        self.gelen_çerçeve = tk.LabelFrame(self.ekran , text = "Gelen Malzeme Bilgileri" , labelanchor= tk.N,
                                           font = self.mini_font  , bd  = 3 , relief= "groove")
        self.gelen_çerçeve.grid(row = 1 , column = 0 , padx = 10 , pady = 10  , ipadx = 10 , ipady = 10)

        self.gln_mlz_hmmd_label = self.label_oluştur(self.gelen_çerçeve , "Gelen Malzeme Hammaddesi: " , 0 , 0 )
        self.gln_mlz_hmmd_combo = ttk.Combobox(self.gelen_çerçeve , values = self.hammade_listesi , textvariable=self.gln_mlz_hmmd_değ, font = self.k_font)
        self.gln_mlz_hmmd_combo.grid(row = 0 , column = 1 , padx = 10 , pady = 10 , sticky = tk.W)


        self.gln_mlz_türü_label = self.label_oluştur(self.gelen_çerçeve , "Gelen Malzeme Türü:",1,0)
        self.gln_mlz_türü_giriş = self.giriş_oluştur(self.gelen_çerçeve , self.gln_mlz_türü_değ , 1 , 1)
        self.gln_mlz_tonaj_label = self.label_oluştur(self.gelen_çerçeve , "Gelen Malzeme Tonaj:" , 2 , 0)
        self.gln_mlz_tonaj_giriş = self.giriş_oluştur(self.gelen_çerçeve , self.gln_mlz_tonaj_değ , 2 , 1)
        self.iş_alış_tarihi_label = self.label_oluştur(self.gelen_çerçeve, "İş Alış Tarihi:", 3, 0)
        self.iş_alış_tarihi_giriş = self.giriş_oluştur(self.gelen_çerçeve, self.iş_alış_tarihi_değ, 3, 1)
        self.sorumlu_kişi_label = self.label_oluştur(self.gelen_çerçeve, "Sorumlu Kişi:", 4, 0)
        self.sorumlu_kişi_giriş = self.giriş_oluştur(self.gelen_çerçeve, self.sorumlu_kişi_değ, 4, 1)
        self.sorumlu_kişi_iletişim_label = self.label_oluştur(self.gelen_çerçeve, "Sorumlu Kişi İletişim:", 5, 0)
        self.sorumlu_kişi_iletişim_giriş = self.giriş_oluştur(self.gelen_çerçeve, self.sorumlu_iletişim_değ , 5 ,  1)

        # ___________________________________________________________________________________________________________
        # GİDEN MALZEME BİLGİLERİ ÇERÇEVESİ TANIMLANIYOR
        self.giden_çerçeve = tk.LabelFrame(self.ekran, text="Giden Malzeme Bilgileri", labelanchor=tk.N,
                                           font=self.mini_font, bd=3, relief="groove")
        self.giden_çerçeve.grid(row=1, column=1, padx=10, pady=10 , ipadx = 10 , ipady = 10)

        self.gdn_mlz_türü_label = self.label_oluştur(self.giden_çerçeve, "Giden Malzeme Türü: ", 0, 0)
        # buraya COMBOBOX GELECEK
        self.gdn_mlz_tonaj_label = self.label_oluştur(self.giden_çerçeve, "Giden Malzeme Tonaj: ", 1, 0)
        self.gdn_mlz_tonaj_giriş = self.giriş_oluştur(self.giden_çerçeve, self.gdn_mlz_tonaj_değ, 1, 1)

        self.iş_teslim_tarihi_label = self.label_oluştur(self.giden_çerçeve, "İş Teslim Tarihi: ", 2, 0)
        self.iş_teslim_tarihi_giriş = self.giriş_oluştur(self.giden_çerçeve, self.iş_teslim_tarihi_değ, 2 ,  1)

        self.karşı_sorumlu_label = self.label_oluştur(self.giden_çerçeve, "Sorumlu (Karşı Taraf) : ", 3, 0)
        self.karşı_sorumlu_giriş = self.giriş_oluştur(self.giden_çerçeve, self.karşı_kişi_değ, 3, 1)

        self.karşı_sorumlu_iletişim_label = self.label_oluştur(self.giden_çerçeve, "Sorumlu İletişim : ", 4, 0)
        self.karşı_sorumlu_iletişim_giriş = self.giriş_oluştur(self.giden_çerçeve, self.karşı_sorumlu_iletişim_değ , 4, 1)

        self.iş_teslim_durumu_label = self.label_oluştur(self.giden_çerçeve, "İş Teslim Durumu:", 5, 0)
        self.iş_devam_rdbtn = tk.Radiobutton(self.giden_çerçeve, text="Devam Ediyor", font=self.k_font,
                                             variable=self.iş_durumu_değ, value=False)
        self.iş_devam_rdbtn.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
        self.iş_teslim_rdbtn = tk.Radiobutton(self.giden_çerçeve, text="Teslim Edildi", font=self.k_font,
                                              variable=self.iş_durumu_değ, value=True)
        self.iş_teslim_rdbtn.grid(row=6, column=1, padx=10, pady=(0, 10), sticky=tk.W)

    # Label Oluşturan Metod
    def label_oluştur(self ,ekran_adı ,  yazı , satır ,sütun ):
        etiket = tk.Label(ekran_adı , text = yazı , font = self.k_font )
        etiket.grid(row = satır , column = sütun , padx = 10 , pady = 10 , sticky = tk.E)
        return etiket

    # Entry leri oluşturan metod
    def giriş_oluştur(self, ekran , değişken,  satır ,sütun ):
        giriş = tk.Entry(ekran , textvariable= değişken , font = self.k_font ,width = 30)
        giriş.grid(row = satır , column = sütun , padx =(0 , 10)  , pady = 10 )
        return giriş

    def tuş_oluştur(self , ekran , yazı , satır , sütun):
        tuş = tk.Entry(ekran , text = yazı , font = self.orta_font)
        tuş.grid(row = satır , column = sütun , padx = 10 , pady = 10)
        return tuş



    def ekran_döngü(self):
        self.ekran.mainloop()


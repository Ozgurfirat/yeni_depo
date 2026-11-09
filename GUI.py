import tkinter as tk
from Sipariş_classı import Sipariş

class Ana_ekran:
    def __init__(self ):
        self.ekran = tk.Tk()
        self.ekran.geometry("800x600+450+100")
        self.ekran.title("_ _ _ _    Siapriş ve Üretim Takip Otomasyonu    _ _ _ _" )
        self.orta_font = ("Helvetica bold" , 17)
        self.k_font = ("Helvetica italic" ,  15)
        self.b_font = ("Helvetica bold" , 19)

        # şirket adı yazılyor
        self.firma_adı_label = self.label_oluştur(self.ekran , str(Sipariş.kuruluş_adı) , 0 , 0)
        self.firma_adı_label.grid_configure(columnspan=5 , sticky= tk.EW)
        self.firma_adı_label.config( font = self.b_font)


        self.gelen_mazleme_label = self.label_oluştur(self.ekran , "Gelen Malzeme: " , 1 , 0 )




    # Label Oluşturan Metod
    def label_oluştur(self ,ekran_adı ,  yazı , satır ,sütun ):
        self.etiket = tk.Label(ekran_adı , text = yazı , font = self.orta_font )
        self.etiket.grid(row = satır , column = sütun , padx = 10 , pady = 10)
        return self.etiket


    def ekran_döngü(self):
        self.ekran.mainloop()


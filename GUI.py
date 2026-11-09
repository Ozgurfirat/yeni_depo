import tkinter as tk


class Ana_ekran:
    def __init__(self ):
        self.ekran = tk.Tk()
        self.orta_font = ("Helvetica bold 17")
        self.k_font = ("Helvetica italic 15")
        self.b_font = ("Helvetica bold 19")





    def label_oluştur(self ,ekran_adı ,  yazı , satır ,sütun ):
        self.etiket = tk.Label(ekran_adı , text = yazı , font = self.orta_font )
        self.etiket.grid()




    def ekran_döngü(self):
        self.ekran.mainloop()




class Sipariş:
    index = 0
    sipariş_listesi = []
    def __init__(self , mlz_hammadde = "?",
                 gelen_mlz_türü = "?" , giden_mlz_türü = "?",
                 gelen_mlz_tonaj = 0 , giden_mlz_tonaj = 0 ,
                 iş_alış_tarihi = "?" , iş_teslim_tarihi = "?",
                 yerel_sorumlu_kişi = "?", yerel_sorumlu_iletişim ="?",
                 karşı_sorumlu_kişi="?", karşı_sorumlu_iletişim="?" ,
                 sipariş_durumu = "Teslim Edilmedi"
                 ):

        self.mlz_hammadde = mlz_hammadde
        self.gelen_mlz_türü = gelen_mlz_türü
        self.giden_mlz_türü = giden_mlz_türü
        self.gelen_mlz_tonaj = gelen_mlz_tonaj
        self.giden_mlz_tonaj = giden_mlz_tonaj
        self.iş_alış_tarihi = iş_alış_tarihi
        self.iş_teslim_tarihi = iş_teslim_tarihi
        self.teslimata_kalan_gün = " ? "
        self.yerel_sorumlu_kişi = yerel_sorumlu_kişi
        self.yerel_sorumlu_iletişim = yerel_sorumlu_iletişim
        self.karşı_sorumlu_kişi =karşı_sorumlu_kişi
        self.karşı_sorumlu_iletişim = karşı_sorumlu_iletişim
        self.kuruluş_adı = "Can Metal Endüstri Ltd. Şti."
        self.sipariş_durumu = sipariş_durumu






class Sipariş:
    İndex = 0
    sipariş_listesi = []
    kuruluş_adı = "Can Metal Endüstri Ltd. Şti."

    def __init__(self , mlz_hammadde : str = "?" , gelen_mlz_türü : str = "?" , giden_mlz_türü : str = "?" , gelen_mlz_tonaj : int = 0 , giden_mlz_tonaj : int = 0 , iş_alış_tarihi : str = "?" , iş_teslim_tarihi : str = "?" , yerel_sorumlu_kişi : str = "?" , yerel_sorumlu_iletişim : str = "?" , karşı_sorumlu_kişi : str = "?" , karşı_sorumlu_iletişim : str = "?" , sipariş_durumu : str = "Teslim Edilmedi"):
        self.mlz_hammadde = mlz_hammadde
        self.gelen_mlz_türü = gelen_mlz_türü
        self.giden_mlz_türü = giden_mlz_türü
        self.gelen_mlz_tonaj = gelen_mlz_tonaj
        self.giden_mlz_tonaj = giden_mlz_tonaj
        self.iş_alış_tarihi = iş_alış_tarihi
        self.iş_teslim_tarihi = iş_teslim_tarihi
        self.teslim_kalan_gün = "?"
        self.terel_sorumlu_kişi = yerel_sorumlu_kişi
        self.yerel_sorumlu_iletişim = yerel_sorumlu_iletişim
        self.karşı_sorumlu_kişi = karşı_sorumlu_kişi
        self.karşı_sorumlu_iletişim = karşı_sorumlu_iletişim
        self.sipariş_durumu = sipariş_durumu
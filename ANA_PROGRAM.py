
from GUI import *
from SİPARİŞ_CLASSI import Sipariş

if __name__ == "__main__":
    Uygulama = Ana_Ekran()

    s1 = Sipariş()
    print(s1.__dict__)

    Uygulama.ekran_döngü()
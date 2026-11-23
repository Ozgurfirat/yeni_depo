
from GUI import *
from Sipariş_classı import Sipariş

if __name__ == "__main__":


    Uygulama = Ana_ekran()

    s1 = Sipariş(mlz_hammadde= "Bakır" , yerel_sorumlu_kişi= "Ali")
    # s2 = Sipariş()
    # s3 = Sipariş()
    # s4 = Sipariş()
    print(s1.__dict__)
    print(s1.__dict__.get("mlz_hammadde"))
    print(s1.__dict__)

    Uygulama.ekran_döngü()
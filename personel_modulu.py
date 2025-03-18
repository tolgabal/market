class personel_modulu:
    def __init__(self,mus_destek="",reyon_bakım="",stok_islemleri="",nobet_cizelge="",izinler="",maas_tablosu=""):
        self.mus_destek=mus_destek,
        self.reyon_bakım=reyon_bakım,
        self.stok_islemleri=stok_islemleri,
        self.nobet_cizelge=nobet_cizelge,
        self.izinler=izinler,
        self.maas_tablosu=maas_tablosu
                
    def mus_destek(self):
       input("Lütfen şikayetinizi belirtiniz.")      
       print("şikayetiniz başarıyla alındı.")
       
    def reyon_bakım(self):
        input("düzeltilmesini istediğiniz reyon numarasını giriniz.")
        print("başarıyla reyon numarası alındı")
        
    def stok_islemleri(self):
        input("stok numarasını giriniz")
        print("stok numarası basarıyla alondı")

    def nobet_cizelge(self):
        print(self.nobet_cizelge)

    def izinler(self):
        print(self.izinler)
    
    def maas_tablosu(self):
        print(self.maas_tablosu)

        
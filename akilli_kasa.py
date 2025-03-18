import tarti


class AkilliKasa:
    def __init__(self, islem, urun, odeme, tutar, miktar, miktar_type):
        self.islem = islem
        self.urun = urun
        self.odeme = odeme
        self.tutar = tutar
        self.miktar = miktar
        self.miktar_type = miktar_type
        self.tarti = tarti()
    
    def urun_satis(self):
        print("Aldiginiz urunler: ", self.urun, "Miktar: ", self.miktar, self.miktar_type)
        print(f"{self.odeme} şeklinde yapacaginiz odeme tutari: ", self.tutar)

    def urun_iade(self):
        print("Iade ettiginiz urunler: ", self.urun)
        print(f"{self.tutar} odediginiz miktar iade ediliyor.")

    
    def urun_miktari(self):
        if self.miktar_type == "kg":
            self.tarti.kg = self.miktar
        elif self.miktar_type == "adet":
            self.tarti.adet = self.miktar
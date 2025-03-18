class SatisRaporu:
    def __init__(self, haftalik, gunluk, urun_miktari):
        self.haftalik = haftalik
        self.gunluk = gunluk
        self.urun_miktari = urun_miktari

    def haftalik_rapor(self):
        print("Bu haftalik satis tutari : ", 12000)

    def gunluk_rapor(self):
        print("Bugunku satis tutari : ", 2000)

    def stok_miktari(self):
        print("Stokta kalan urun miktari : ", 1000-self.urun_miktari)
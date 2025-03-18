import tarti
class Pastane:
    def __init__(self,miktar,miktar_type):
        self.miktar = miktar
        self.miktar_type = miktar_type
        self.tarti = tarti()
        
        
    def adet(self):
        if self.miktar_type == "kg":
            self.tarti.kg = self.miktar
        elif self.miktar_type == "adet":
            self.tarti.adet = self.miktar
            
        
            
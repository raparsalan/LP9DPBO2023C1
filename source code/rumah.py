from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, jml_penghuni, ukuran, kepemilikan, jml_kamar, foto):
        super().__init__("Rumah",nama_pemilik, nama_penghuni, jml_penghuni, ukuran, kepemilikan, foto)
        self.jml_kamar = jml_kamar

    def get_dokumen(self):
        return "Surat tanah dan bangunann a/n " + self.nama_pemilik +"\n"
    
    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_details(self):
        if(self.kepemilikan == "Pribadi"):
            return self.get_summary()+"Rumah ini milik pribadi\ndimiliki oleh "+ self.nama_pemilik +" dan dihuni oleh : " + self.nama_penghuni + "\n Dengan " + str(self.jml_kamar) + " buah kamar \n Dokumen Bangunan : \n" + self.get_dokumen()
        else:
            return "Rumah ini adalah sewaan\ndimiliki oleh "+ self.nama_pemilik +" dan dihuni oleh : " + self.nama_penghuni + "\n Dengan " + str(self.jml_kamar) + " buah kamar \n Dokumen Bangunan : \n" + self.get_dokumen()
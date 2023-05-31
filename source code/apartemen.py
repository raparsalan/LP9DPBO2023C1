from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, nama_penghuni, ukuran, kepemilikan, jml_kamar, foto):
        super().__init__("Apartemen", nama_pemilik, nama_penghuni, jml_penghuni, ukuran, kepemilikan, foto)
        self.jml_kamar = jml_kamar

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."
    
    def get_jml_kamar(self):
        return self.jml_kamar

    def get_details(self):
        if(self.kepemilikan == "Pribadi"):
            return self.get_summary() + "Apartemen ini milik pribadi\ndimiliki oleh "+ self.nama_pemilik +" \n Dihuni oleh " + self.nama_penghuni + "\n Dengan " + str(self.jml_kamar) + " buah kamar \n Dokumen Bangunan : \n" + self.get_dokumen()
        else:
            return self.get_summary() + "Apartemen ini adalah sewaan\ndimiliki oleh "+ self.nama_pemilik +" dan dihuni oleh : " + self.nama_penghuni + "\n Dengan " + str(self.jml_kamar) + " buah kamar \n Dokumen Bangunan : \n" + self.get_dokumen()
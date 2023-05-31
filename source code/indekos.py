from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, tipe, jml_penghuni, ukuran, kepemilikan, foto):
        super().__init__("Indekos", nama_pemilik, nama_penghuni, jml_penghuni, ukuran, kepemilikan, foto)
        self.tipe = tipe

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_details(self):
        return self.get_summary() + "Pemilik kosan adalah "+ self.nama_pemilik +" dan dihuni oleh : " + self.nama_penghuni + "\n Adalah Kosan "+self.tipe+"\n Dokumen : \n" + self.get_dokumen()
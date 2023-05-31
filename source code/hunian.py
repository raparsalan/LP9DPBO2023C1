class Hunian():
    def __init__(self, jenis, nama_pemilik, nama_penghuni, jml_penghuni, ukuran, kepemilikan, foto):
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.ukuran = ukuran
        self.kepemilikan = kepemilikan
        self.foto = foto; 

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_ukuran(self):
        return self.ukuran

    def get_kepemilikan(self):
        return self.kepemilikan
    
    def get_foto(self):
        return self.foto
    
    def get_dokumen(self):
        pass

    def get_summary(self):
        return self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang.\n Ukuran : " + self.ukuran + "\n"
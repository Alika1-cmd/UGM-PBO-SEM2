class Mahasiswa:
    nama = ""
    nim = ""
    jurusan = ""

    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama     :", self.nama)
        print("NIM      :", self.nim)
        print("Jurusan  :", self.jurusan)

class MahasiswaS1(Mahasiswa):
    skripsi = ""

    def __init__(self, nama, nim, jurusan, skripsi):
        super().__init__(nama, nim, jurusan)
        self.skripsi = skripsi

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Skripsi  :", self.skripsi) 

mhs1 = MahasiswaS1("Indira", "2201001", "Biologi", "Penerapan kambium dalam Kesehatan")
mhs1.tampilkan_info()

# Menghapus atribut skripsi
del mhs1.skripsi

print("\nSetelah atribut skripsi dihapus:")
mhs1.tampilkan_info() 

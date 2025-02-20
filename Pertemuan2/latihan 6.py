class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

# Meminta input dari pengguna
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
orang = Manusia(nama, umur)

print("\nInformasi Manusia:")
orang.tampilkan_data()

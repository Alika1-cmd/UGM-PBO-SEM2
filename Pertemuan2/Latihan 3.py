# Mendefinisikan kelas Persegi
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi**2

    def hitung_keliling(self):
        return self.sisi*4

# Meminta input panjang sisi dari pengguna
sisi = int(input("Masukkan panjang sisi persegi: "))

# Membuat objek Persegi dengan nilai input dari pengguna
square = Persegi(sisi)

# Menampilkan hasil
print(f"\nPersegi dengan sisi {square.sisi} memiliki")
print(f"Luas    : {square.hitung_luas()}")
print(f"Keliling: {square.hitung_keliling()}")

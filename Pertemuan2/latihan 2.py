# Mendefinisikan kelas Hewan
class Hewan:
    def __init__(self, nama, suara):
        self.nama = nama  
        self.suara = suara  

    def buat_suara(self):
        print(f"{self.nama} suaranya : {self.suara}")

# Membuat objek dari kelas Hewan
kucing = Hewan("Kucing", "Meong")
bebek = Hewan("bebek", "kwek kwek")

# Memanggil metode buat_suara
kucing.buat_suara()
bebek.buat_suara()

class Rekening:
    def __init__(self, nama_nasabah, no_rekening, saldo_rekening):
        self.nama = nama_nasabah
        self.no_rekening = no_rekening
        self.saldo = saldo_rekening

class Nasabah(Rekening):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", int(self.no_rekening))
        print("Saldo: Rp" + str(float(self.saldo)))
        print()


nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

print("Data Nasabah")
print()
print("=== Rekening Nasabah 1 ===")
nasabah1.tampilkan_data()
print()
print("=== Rekening Nasabah 2 ===")
nasabah2.tampilkan_data()

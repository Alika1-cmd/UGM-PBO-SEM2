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

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print("Setor tunai " + self.nama + " telah berhasil sebesar Rp" + str(jumlah) + " berhasil.")

    def tarik_tunai(self, jumlah):
        self.saldo -= jumlah
        print("Tarik tunai " + self.nama + " telah berhasil sebesar Rp" + str(jumlah) + " berhasil.")

nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

print("Data Nasabah")
print()
print("=== Rekening Nasabah 1 ===")
nasabah1.tampilkan_data()
print("=== Rekening Nasabah 2 ===")
nasabah2.tampilkan_data()

print("=== Transaksi Setor/Tarik Tunai ===")
nasabah1.setor_tunai(1000000)
nasabah2.tarik_tunai(1000000)
print()

print("=== Data Nasabah Setelah Transaksi ===")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()

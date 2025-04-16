
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp{:,.0f}".format(self.saldo))
        print()

nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

print("=== Data Nasabah Awal ===")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()


#  Lanjutan Program Soal nomor 5

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp{:,.0f}".format(self.saldo))
        print()

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai sebesar Rp{jumlah:,} berhasil.")

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk tarik tunai.")
        else:
            self.saldo -= jumlah
            print(f"Tarik tunai sebesar Rp{jumlah:,} berhasil.")

print("=== Transaksi Setor/Tarik Tunai ===")
nasabah1.setor_tunai(1000000)  
nasabah2.tarik_tunai(1000000)  
print()

print("=== Data Nasabah Setelah Transaksi Setor/Tarik ===")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()


# Lanjutan Program Soal nomor 6 

class Nasabah(Rekening):
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("No. Rekening:", self.no_rekening)
        print("Saldo: Rp{:,.0f}".format(self.saldo))
        print()

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai sebesar Rp{jumlah:,} berhasil.")

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk tarik tunai.")
        else:
            self.saldo -= jumlah
            print(f"Tarik tunai sebesar Rp{jumlah:,} berhasil.")

    def transfer(self, penerima, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk transfer.")
        else:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            print(f"Transfer sebesar Rp{jumlah:,} dari rekening {self.no_rekening} ke rekening {penerima.no_rekening} berhasil.")

nasabah1 = Nasabah("Budi", 5555, 1500000)  
nasabah2 = Nasabah("Wati", 6666, 1000000)  
print("=== Transaksi Transfer ===")
nasabah1.transfer(nasabah2, 500000)
print()

print("=== Data Nasabah Setelah Transfer ===")
nasabah1.tampilkan_data()
nasabah2.tampilkan_data()

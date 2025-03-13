class Tiket:
    def __init__(self, kategori, harga_jual):
        self.kategori = kategori
        self.harga_jual = harga_jual 
        
    def __mul__(self, banyak_penjualan):
        print('Jumlah tiket terjual:', banyak_penjualan.jumlah_tiket, 'tiket')
        return self.harga_jual * banyak_penjualan.jumlah_tiket


class Penjualan_Tiket:
    def __init__(self, kategori, jumlah_tiket):
        self.kategori = kategori
        self.jumlah_tiket = jumlah_tiket

eksklusif = Tiket("Eksklusif", 9000) 
total_penjualan_mingguan = Penjualan_Tiket("Eksklusif", 20)  

print(f"Total pendapatan dari {eksklusif.kategori}: {eksklusif * total_penjualan_mingguan} ribu")

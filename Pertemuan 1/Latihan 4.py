class Tiket:
    def __init__(self, kategori, harga_satuan):
        self.kategori = kategori
        self.harga_satuan = harga_satuan 
        
    def __mul__(self, penjualan):
        print('Jumlah tiket terjual:', penjualan.jumlah_tiket, 'tiket')
        return self.harga_satuan * penjualan.jumlah_tiket


class PenjualanTiket:
    def __init__(self, kategori, jumlah_tiket):
        self.kategori = kategori
        self.jumlah_tiket = jumlah_tiket

eksklusif = Tiket("Eksklusif", 9000)  
penjualan_maret = PenjualanTiket("Eksklusif", 20) 

print(f"Total pendapatan dari kategori {eksklusif.kategori}: {eksklusif * penjualan_maret} ribu")

class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id]
    
        
    class Mahasiswa(Orang):
        SARJANA = "SARJANA"
        MASTER = "MASTER"
        DOKTOR = "DOKTOR"
        def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
            super().__init__(nama_depan, nama_belakang, nomor_id)
            self.jenjang = jenjang
            self.matkul = []
        def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
        
    class Karyawan(Orang):
        TETAP = "TETAP"
        TDK_TETAP = "TDK_TETAP"
         def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan): 
            super().__init__(nama_depan, nama_belakang, nomor_id)
            self.status_karyawan = status_karyawan
            
        class Dosen(Karyawan):
        def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
            super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
            self.matkul_diajar = []
        def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
bowo.tampilkan_info()
bowo.tampilkan_matkul()    

rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")
rizki.tampilkan_info()
rizki.tampilkan_matkul_diajar()

class Pelajar:
    def __init__(self):
        self.matkul = []

class Pelajar:
    def __init__(self):
        self.matkul = []
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
        
class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

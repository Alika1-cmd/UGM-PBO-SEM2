class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
    
  class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = range(3)

    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []
    
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        self.status_karyawan = status_karyawan

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs)
        self.matkul_diajar = []
    
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")

rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")

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

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs):
        Orang.__init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
        
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

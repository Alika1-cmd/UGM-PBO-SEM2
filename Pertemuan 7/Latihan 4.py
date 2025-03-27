def add_attendance(cls):
    """menambahkan fitur absensi ke dalam kelas."""
    
    def mark_attendance(self):
        print(f"{self.name} telah hadir di sekolah hari ini.")
    
    cls.absen = mark_attendance  
    return cls

@add_attendance
class Siswa:
    def __init__(self, nama, kelas):
        self.name = nama
        self.kelas = kelas

    def info(self):
        print(f"Saya {self.name} dari kelas {self.kelas}.")

# Membuat objek siswa
siswa1 = Siswa("Gadis", "10 IPA 3")
siswa2 = Siswa("Alika", "10 IPA 5")

# Memanggil method asli dari kelas
siswa1.info()
siswa2.info()

# Memanggil method yang ditambahkan oleh decorator
siswa1.absen()
siswa2.absen()

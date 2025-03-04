class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")

mhs1 = Mahasiswa("indira", "22012345")
mhs1.tampilkan_info()

delattr(mhs1, "nim")

print("\nSetelah atribut 'nim' dihapus:")
try:
    mhs1.tampilkan_info()
except AttributeError as e:
    print(f"Terjadi error: {e}")

del mhs1

print("\nSetelah objek dihapus:")
try:
    mhs1.tampilkan_info()
except NameError as e:
    print(f"Terjadi error: {e}")

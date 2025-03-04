class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")

mhs1 = Mahasiswa("indira", "22012345")
print("Sebelum atribut dihapus:")
mhs1.tampilkan_info()

delattr(mhs1, "nim")

print("\nSetelah atribut 'nim' dihapus:")
mhs1.tampilkan_info() 

del mhs1

print("\nSetelah objek dihapus:")
mhs1.tampilkan_info()  

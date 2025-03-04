class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        try:
            print(f"Nama: {self.nama}, NIM: {self.nim}")
        except AttributeError:
            print("Atribut telah dihapus dan tidak bisa diakses.")

mhs1 = Mahasiswa("Indira", "22012345")
mhs1.tampilkan_info()

del mhs1.nim

print("\nSetelah atribut 'nim' dihapus:")
try:
    print(f"NIM: {mhs1.nim}")  # Ini akan menyebabkan AttributeError
except AttributeError:
    print("Error: Atribut 'nim' telah dihapus.")

del mhs1

print("\nSetelah objek dihapus:")
try:
    mhs1.tampilkan_info()  # Ini akan menyebabkan NameError
except NameError:
    print("Error: Objek telah dihapus dan tidak bisa diakses.")

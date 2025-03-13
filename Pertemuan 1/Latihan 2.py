class Alat_musik:
    def buat_suara(self):
        print("Alat musik bisa mengeluarkan banyak suara.")

class Gitar(Alat_musik):
    def buat_suara(self):
        print("Gitar : Jreeeng!...")

class Drum(Alat_musik):
    def buat_suara(self):
        print("Drum : Dung... Tak...")

gitar = Gitar()
drum = Drum()

# Menggunakan polimorfisme
for Alat_musik in (gitar, drum):
    Alat_musik.buat_suara()

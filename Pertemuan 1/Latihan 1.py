class Gitar:
    def bunyi_suara(self):
        print("Gitar : Jreeeng!...")

    def tipe(self):
        print("Gitar adalah alat musik petik.")


class Drum:
    def bunyi_suara(self):
        print("Drum : Dung... Tak...")

    def tipe(self):
        print("Drum adalah alat musik pukul.")

Gitar = Gitar()
Drum = Drum()

# Menggunakan polimorfisme
for Alat_musik in (Gitar, Drum):
    Alat_musik.bunyi_suara()
    Alat_musik.tipe()

class Koordinat2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Koordinat3D(Koordinat2D):
    z = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def tampilkan_koord(self):
        print('x =', self.x)
        print('y =', self.y)
        print('z =', getattr(self, 'z', 'Tidak Ada'))  # Cek apakah z ada

titik1 = Koordinat3D(1, 2, 3)
titik1.tampilkan_koord()

delattr(titik1, 'z')
print("\nEfek fungsi delattr()")
titik1.tampilkan_koord() 

del titik1.y
print("\nEfek keyword del")
try:
    titik1.tampilkan_koord()
except AttributeError as e:
    print(f"Terjadi error: {e}")

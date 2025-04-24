from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])
titik1 = Koordinat(x=2, y=4)

#menggunakan indeks elemen
print("x =", titik1[0])
print("y =", titik1[1])

#menggunakan field name 
print("x =", titik1.x)
print("y =", titik1.y)

#menggunakan getattr()
print("x =", getattr(titik1,'x'))
print("y =", getattr(titik1,'y'))

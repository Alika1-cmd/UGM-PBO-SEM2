# Fungsi menghitung keliling dan luas lingkaran tanpa import
def hitung_lingkaran(jari_jari):
    pi = 3.14159
    keliling = 2 * pi * jari_jari
    luas = pi * (jari_jari ** 2)
    return keliling, luas

# Program utama
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
keliling, luas = hitung_lingkaran(jari_jari)
print(f"Keliling: {keliling:.2f}")
print(f"Luas: {luas:.2f}")

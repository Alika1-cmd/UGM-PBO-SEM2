# Fungsi untuk menampilkan hitungan mundur dari number hingga 0.
def hitung_mundur(number):
    while number >= 0:  
        print(number, end=" ")  
        number -= 1  

# Program utama
angka = int(input("Masukkan angka: "))  
hitung_mundur(angka)  

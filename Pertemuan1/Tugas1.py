def hitung_mundur(number):
    """Fungsi untuk menampilkan hitungan mundur dari n hingga 0."""
    while number >= 0:  
        print(number, end=" ")  
        number -= 1  

# Program utama
angka = int(input("Masukkan angka: "))  
hitung_mundur(angka)  

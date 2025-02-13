# Fungsi untuk mengklasifikasi suhu
def klasifikasi_suhu(suhu):
    if suhu < 0:
        return "Membeku"
    elif suhu < 10:
        return "Sangat Dingin"
    elif suhu < 20:
        return "Sejuk"
    elif suhu < 30:
        return "Hangat"
    elif suhu < 40:
        return "Panas"
    else:
        return "Sangat Panas"

# Program utama
suhu = float(input("Masukkan suhu dalam derajat Celcius: "))
kategori = klasifikasi_suhu(suhu)
print(f"Suhu {suhu}°C dikategorikan sebagai: {kategori}")

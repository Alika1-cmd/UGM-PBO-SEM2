# def menentukan huruf nilai
def tentukan_huruf(nilai):
    if 80 <= nilai <= 100:
        return "A"
    elif 70 <= nilai < 80:
        return "B"
    elif 60 <= nilai < 70:
        return "C"
    elif 50 <= nilai < 60:
        return "D"
    else:
        return "E"

# Program utama
niu = input("Masukkan NIU (6 digit): ")
tugas = float(input("Masukkan nilai tugas: "))
laporan = float(input("Masukkan nilai laporan: "))
rata_rata = (tugas + laporan) / 2

#ketentuan 
if rata_rata < 40:
    print(f"Siswa dengan NIU {niu} mendapat nilai: K")
else:
    ujian = float(input("Masukkan nilai ujian: "))
    nilai_akhir = (0.25 * tugas) + (0.25 * laporan) + (0.50 * ujian)
    huruf = tentukan_huruf(nilai_akhir)
    print(f"Siswa dengan NIU {niu} mendapat nilai akhir: {nilai_akhir} ({huruf})")

# Program Seleksi Mandiri Mahasiswa
from abc import ABC, abstractmethod

class Universitas(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def Ujian_Mandiri(self):
        pass

class UGM(Universitas):
    def Ujian_Mandiri(self):
        return "Utul UGM"

class UI(Universitas):
    def Ujian_Mandiri(self):
        return "Simak UI"

class ITB(Universitas):
    def Ujian_Mandiri(self):
        return "SM-ITB"

def tipe_ujian_mandiri(Universitas):
   print(Universitas.nama, "masuk melalui seleksi:", Universitas.Ujian_Mandiri())

Mahasiswa1 = UGM("Alika")
Mahasiswa2 = UI("Silvia")
Mahasiswa3 = ITB("Eriza")

tipe_ujian_mandiri(Mahasiswa1) 
tipe_ujian_mandiri(Mahasiswa2) 
tipe_ujian_mandiri(Mahasiswa3)  

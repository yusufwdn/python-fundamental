# Inheritance (Pewarisan)
# Merupakan sebuah istilah yang digunakan untuk menggambarkan sebuah kelas yang dapat menurunkan
# atribut dan method yang dimiliki kelas induk kepada kelas anak.

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil): # Implementasi kode ketika kelas MobilSport merupakan anak dari kelas Mobil
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Hijau", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Ungu", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

"""
Output:
160
160
210
"""
# Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah 
# adanya parameter self yang merujuk pada objek saat ini.
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobilBaru = Mobil("Merah", "Honda", 160)
print("Sebelum ditambahkan: ")
print(mobilBaru.kecepatan)

mobilBaru.tambah_kecepatan() # Memanggil method tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobilBaru.kecepatan)
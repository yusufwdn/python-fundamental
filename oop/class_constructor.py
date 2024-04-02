# Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang 
# digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas. 

# Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, 
# hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.

class Mobil:
    # Deklarasi constructor dalam sebuah kelas
    def __init__(self):
        # Kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang 
        # sedang diproses saat ini.
        self.warna = 'Merah'

# Membuat instance objek
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

"""
Output:
Merah
Merah
Hitam
Merah
"""
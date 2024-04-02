# Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. 

# Jika object method identik dengan parameter self yang merujuk pada objek, class method juga 
# memerlukan sebuah parameter yang merujuk pada kelas.

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

# Pada bagian fungsi intro_mobil, kita menambahkan parameter cls. Ini adalah parameter wajib 
# dalam menggunakan dekorator @classmethod.
        
# Catatan:
# Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan 
# kode. Anda dapat mengganti namanya, tidak harus cls.
        
Mobil.intro_mobil()
mobil_1 = Mobil("Nissan GTR")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""
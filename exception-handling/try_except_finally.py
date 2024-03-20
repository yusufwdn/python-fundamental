var_dict = {"skor akhir": "8.2"}

try:
    print(f"skor akhir {var_dict['score']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Baris ini dieksekusi jika tidak ada exception.")
finally:
    print("Baris ini dieksekusi tanpa peduli ada exception atau tidak.")
    
"""
Output:
skor akhir 8.2
Baris ini dieksekusi jika tidak ada exception.
Baris ini dieksekusi tanpa peduli ada exception atau tidak.
"""
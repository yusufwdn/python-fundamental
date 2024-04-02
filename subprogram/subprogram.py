# Subprogram

# Subprogram digunakan agar kita tidak perlu mengetik script yang sama berulang-ulang.
# Jadi kita bisa menggunakan fungsi yang dapat digunakan berulang-ulang, kita tinggal
# memanggilnya saja dengan mengisi parameter yang diperlukan (jika ada)

# Mendeklarasikan fungsi untuk menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil

# Memanggil 'luas_persegi_panjang' dengan parameter 'panjang' = 4 dan 'lebar' = 13
hasil_x = luas_persegi_panjang(4, 13)
print(hasil_x)

# Memanggil 'luas_persegi_panjang' dengan parameter 'panjang' = 7 dan 'lebar' = 17
hasil_y = luas_persegi_panjang(7, 17)
print(hasil_y)

"""
Output:
52
119
"""
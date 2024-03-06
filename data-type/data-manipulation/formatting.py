"""============ FORMATTING ============"""

# zfill()
# Digunakan untuk menambahlan nilai 0 di depan sebuah string dengan panjang tertentu
word = 'Adventure'
add_number = word.zfill(20)
print(add_number)

# rjust() & ljust()
# Digunakan untuk merapikan pencetakan teks, rjust rata kanan, ljust rata kiri.
print('Python Development'.rjust(20))
print('Happier'.ljust(20, '!'))

# Center
# Digunakan untuk merapikan pencetakan teks agar teks berada di tengah-tengah
print('Bukan Judul Lagu'.center(24, '='))

# String Literal
print("Halo!\nBagaimana kabarmu? Apakah baik-baik saja?\nKita bertemu hari Jum\'at bulan Mei.")

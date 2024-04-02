# Sederhananya, object merupakan wujud yang merepresentasikan class.
class Mobil:
    # Atribut
    warna = "Hitam"

# Ini merupakan sebuah object
mobilku = Mobil()
print(mobilku.warna) # Memanggil attribut 'warna' milik kelas 'Mobil'

# Merubah value dari attribut class
mobilku.warna = "Putih"
print(mobilku.warna)

"""
Output:
Hitam
"""
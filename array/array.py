"""============ ARRAY ============"""
"""
    Array adalah salah satu jenis dari struktur data linear. Dalam konteks ini, array terdiri dari 
    kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear. 
    
    Sebenarnya kalau di Python disebut dengan List, tapi kita akan asumsikan bahwa List disebut juga
    dengan array.
"""

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])


"""
Output:
[90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
90
"""

# Mengisi nilai array dengan value menggunakan for range
var_arr = [0 for i in range(10)]
for i in range(10):
    var_arr[i] = i

print(var_arr)


"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# Mengakses array berdasarkan indeksnya
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])

"""
Output:
9
"""
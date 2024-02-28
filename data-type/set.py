# Set adalah kumpulan item yang bersifat unik, tanpa urutan, dan dapat diinisialisasikan
# dengan kurawal "{}" dimana setiap elemennya dipisahkan dengan koma.

# Set akan menghilangkan data yang duplikat, ketika memang ada data duplikat di dalamnya. 
# Oleh karena itu kita dapat menggunakan set untuk menghilangkan duplikasi dalam sebuah kumpulan item.
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""


# Di dalam set, kita tidak melakukan metode indexing seperti di list dan tuple, karena
# set tidak memiliki indeks (item bersifat unik dan tanpa urutan).

x = {1,2,7,2,3,13,3}
# print(x[0]) # jika ingin melihat output error, hilangkan komen di paling kiri

"""
Output:
'set' object is not subscriptable
"""

# Kita dapat melakukan operasi gabungan (union) dan irisan (intersection) dalam set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Menggabungkan set1 dan set2
union = set1.union(set2)
print("Union:", union)

# Hanya menggabungkan nilai yang sama antara set1 dan set2 (irisan)
intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""
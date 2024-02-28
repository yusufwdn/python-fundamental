"""
    Dictionary

    Merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan 
    untuk menyimpan data kecil hingga besar.
"""

# contoh dictionary
dict = { 'name': 'Jackie Chan', 'age': 36, 'isMarried': True }

print(type(dict))

"""
Output:
<class 'dict'>
"""

# Tidak seperti list yang mendapatkan value menggunakan index, value pada dictionary 
# didapatkan dengan syarat kita harus mengetahui key-nya.

# dict[0] # ini akan error, karena pada dictionary di atas tidak ada yang key-nya 0.

# Berikut contoh get value dari key 'name'
print(dict['name'])

"""
Output:
Jackie Chan
"""

# Kita juga bisa menambahkan data ke dalam dictionary dengan cara berikut
dict["address"] = "Jakarta Utara"

print(dict)

"""
Output:
{'name': 'Jackie Chan', 'age': 36, 'isMarried': True, 'address': 'Jakarta Utara'}
"""

# Selain menambahkan, kita juga dapat menghapus data dari dictionary
del dict['isMarried']

print(dict)

"""
Output:
{'name': 'Jackie Chan', 'age': 36, 'address': 'Jakarta Utara'}
"""

# Contoh script untuk mengubah data di dalam dictionary
dict["address"] = "Kota Bogor"

print(dict)

"""
Output:
{'name': 'Jackie Chan', 'age': 36, 'address': 'Kota Bogor'}
"""
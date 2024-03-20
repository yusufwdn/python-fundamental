"""============ LOOPING ============"""
"""
     Looping (perulangan) merupakan sebuah metode dimana kita mengulang aksi dari 
     suatu kode program sebanyak yang diinginkan.
"""

# Menampilkan nilai tanpa looping
print(" Tanpa looping ".center(30,"-"))
print(1)
print(2)
print(3)
print(4)
print(5)

"""
Output:
1
2
3
4
5
"""

# Menampilkan nilai dengan looping (for)
print(" Perulangan For ".center(30,"-"))
numbers = [1,2,3,4,5]
for i in numbers :
    print(i)

# Menampilkan nilai dengan looping (range)
print(" Perulangan Range ".center(30,"-"))
# Penjelasan range = range(start,stop,step)
# Script tersebut dapat diartikan bahwa pada parameter pertama itu mulai perulangan
# dari angka berapa, di parameter kedua diindikasikan sebagai angka pemberhentian
# proses perulangan, dan yang ketiga digunakan untuk 'melangkahi' sejumlah angka 
# (contoh di bawah ini melangkah 2 angka kedepan)
for i in range(1,10,2):
    print(i)


# Menampilkan nilai dengan looping (while)
print(" Perulangan While ".center(30,"-"))
counter = 1
# Penjelasan: Selama counter tidak bernilai 5, maka perulangan akan terus berlangsung
while counter <= 5:
    print(counter)
    counter += 1
    
    # Digunakan untuk menambahkan value pada counter. Jika tidak, akan terjadi infinity loop
    # (perulangan tanpa ujung) dikarenakan kondisi di atas tidak akan terpenuhi dan perulangan 
    # tidak akan berhenti jika counter tetap bernilai 1 (di kondisinya akan berhenti jika counter bernilai 5 atau lebih).

# Menampilkan nilai dengan looping (for di dalam for)
print(" For Dalam For ".center(30,"-"))
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

"""
Output:
1 1
1 2
2 1
2 2
"""

# Kontrol foreach dengan 'break'
# break merupakan sebuah pernyataan menghentikan proses perulangan
print(" Break Statement ".center(30,"-"))
for i in range(3):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

# Kontrol foreach dengan 'continue'
# continue merupakan sebuah pernyataan untuk 'skip' perulangan
print(" Continue Statement ".center(30,"-"))
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""
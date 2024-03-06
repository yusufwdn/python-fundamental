"""============ OPERATION ============"""

# data sample
list_sample   = [1,2,3,6,6,6]
set_sample    = set([1,3,4,6,8,7,9,9.6])
string_sample = "Yo bro, what are you doing?"

# len
# Digunakan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string
print(len(list_sample))     # Output: 6
print(len(set_sample))      # Output: 8
print(len(string_sample))   # Output: 27

# min & max
# Digunakan untuk mendapatkan nilai paling kecil (min) dan nilai paling besar (max)
print(min(list_sample)) # Output: 1
print(max(list_sample)) # Output: 6

# count
# Digunakan untuk menghitung berapa kali objek muncul di dalam list
print(list_sample.count(6))     # Output: 3
print(string_sample.count("o")) # Output: 4

# in & not in
# Digunakan untuk melakukan pengecekan, apakah objek yang kita cari ada di dalam list atau tidak
word = "Ketika mimpimu, yang begitu indah, tak pernah terwujud, yasudahlah."
print("indah" in word)         # Output: True
print("yasudahlah" in word)    # Output: True
print("apalagi" in word)       # Output: False
print("mimpi" in word)         # Output: True
print("wujud" in word)         # Output: True

# assign multiple variables
new_list = ["merah", "kuning", "hijau"]

color1, color2, color3 = new_list

print(color1)
print(color2)
print(color3)

# sort  
# Digunakan untuk mengurutkan angka atau huruf dalam sebuah list

# important notes:
# 1. sort tidak dapat mengurutkan angka dan huruf dalam suat list sekaligus
# 2. sort menggunakan metode ASCII, sehingga teks yang uppercase akan dibandingkan lebih dahulu

brands = ["BMW", "Nissan", "mercedes benz", "dodge", "april"]

print(brands)

brands.sort()
print(brands)
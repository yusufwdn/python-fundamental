"""============ TRANSFORM ============"""

# Mengubah string menjadi uppercase dan lowercase
word = 'i love you'

word = word.upper() # set uppercase
print(word) # Output: I LOVE YOU

word = word.lower() # set lowercase
print(word) # Output: i love you

# Menghapus kelebihan spasi di kanan, kiri dan kanan-kiri dalam sebuah string
print("     HELLO".lstrip())     # Output: Hello
print("HELLO     ".rstrip())     # Output: Hello
print("     HELLO     ".strip()) # Output: Hello

# String STARTSWITH dan ENDSWITH
# Cek value apakah string dimulai dengan suatu kata yang diinginkan dengan menggunakan
# method startswith dan endswith.
# Catatan: Method ini bersifat sensitive case.
print("Saya suka Indonesia".startswith("Saya")) # Output True
print("Saya suka Indonesia".startswith("SaYa")) # Output False
print("Saya suka Indonesia".endswith("Indonesia")) # Output True
print("Saya suka Indonesia".endswith("INDONESIA")) # Output False

# String JOIN
# Digunakan untuk menggabungkan banyak string di dalam list menjadi sebuah string
print(" ".join(["aku", "suka", "kamu"])) # Output: aku suka kamu
print("-".join(["aku", "suka", "kamu"])) # Output: aku-suka-kamu

# String SPLIT
# Digunakan untuk memisahkan kata di dalam string menjadi sebuah list
print("Terus berjuang, jangan menyerah !".split())     # Output: ['Terus', 'berjuang,', 'jangan', 'menyerah', '!']
print("terus-berjuang-,-jangan-menyerah-!".split("-")) # Output: ['Terus', 'berjuang,', 'jangan', 'menyerah', '!']

# String REPLACE
# Digunakan untuk memperbarui string
word = "Aku selalu tidak sekolah"
print(word.replace("tidak ", "")) # Output: "Aku selalu sekolah"

# String ISUPPER
# Digunakan untuk cek apakah string merupakan UPPERCASE
word = "SMOOTH"
print(word.isupper()) # Output: True

# String ISLOWER
# Digunakan untuk cek apakah string merupakan LOWERCASE
word = "smoothies"
print(word.islower()) # Output: True

# String ISALNUM
# Digunakan untuk cek apakah string merupakan alpha numeric
word = "ap4kahb3nar"
print(word.isalnum()) # Output: True

# String ISDECIMAL
# Digunakan untuk cek apakah string merupakan decimal
number = '123'
print(number.isdecimal())

# String ISSPACE
# Digunakan untuk cek apakah string berisi hanya spasi
print("           ".isspace())

# String ISTITLE
# Digunakan untuk mengecek apakah setiap kata di dalam string merupakan huruf kapital
print("Indonesia Raya".istitle())
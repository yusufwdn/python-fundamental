# Pada pembuatan method, sebenarnya kita membuat fungsi di dalam kelas itu sendiri. 
# Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode.

# Python membagi method menjadi tiga jenis.

# - Metode dari object (object method).
# - Metode secara statis (static method).
# - Metode dari class (class method).

# Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja. 
# Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal. Contoh sederhana dekorator sebagai berikut.

def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""

"""
    Konversi

    Merupakan sebuah aktivitas dimana kita dapat merubah dari satu tipe data ke tipe data
    lainnya dengan menggunakan method di dalam python.
"""

# konversi integer ke float
print(float(3))

"""
Output:
3.0
"""

# konversi float ke integer
print(int(2.5))
print(int(-6.66))

"""
Output:
2
6
"""

# konversi dari tipe data `n` ke string
print(int("13"))
print(str(13))
print(float("13"))
print(str(13.6))

"""
Output:
13
13
13.0
13.6
"""

# contoh konversi gagal dari string ke int
# print(int("1p")) # jika ingin melihat errornya, hilangkan komen di paling kiri

"""
Output:
ValueError: invalid literal for int() with base 10: '1p
"""

# konversi data list
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""
"""============ LOGICAL OPERATOR ============"""
"""
    Merupakan jenis operator untuk melakukan operasi logika dengan kedua operannya bertipe boolean.
"""

# AND
# Operator yang menghasilkan True ketika dua nilai perbandingannya bernilai Ture juga.

print(True and True)
print(True and False)
print(False and True)
print(False and False)


"""
Output:

True
False
False
False
"""

# OR
# Operator yang menghasilkan nilai true ketika salah satu dari seluruh perbandingan bernilai true
print(True or True)
print(True or False)
print(False or True)
print(False or False)


"""
Output:

True
True
True
False
"""

# NOT
# Operator yang digunakan untuk membalikan nilai boolean, misal di awal true, dirubah menjadi false.
print(not True)
print(not False)

"""
Output:

False
True
"""
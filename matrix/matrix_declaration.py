# Deklarasi matriks sederhana
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
            
print(matriks)

"""
Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

# Deklarasi matriks dengan nilai default
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)

"""
Output:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""


# Deklarasi matriks menggunakan NumPy
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
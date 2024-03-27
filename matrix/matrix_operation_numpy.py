# Kali ini kita akan mencoba operasi perkalian matriks dengan menggunakan library NumPy

import numpy as np

# Deklarasi matriks 2x2
var_mat = np.array([[5, 0], [1, -2]])

# Kalikan matriks dengan angka 2 (secara langsung)
# Di file matrix_operation.py kita telah mencoba perkalian dengan cara manual yang cukup rumit,
# namun di sini kita dipermudah dengan library NumPy
result = var_mat * 2

print(result)

"""
Output:
[[10  0]
 [ 2 -4]]
"""
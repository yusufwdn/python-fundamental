import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

list_bytes  = sys.getsizeof(var_list) * len(var_list)
numpy_bytes = var_array.size * var_array.itemsize

print("Ukuran keseluruhan elemen list dalam bytes  = ", list_bytes)
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", numpy_bytes)

"""
Output:
Ukuran keseluruhan elemen list dalam bytes  =  240
Ukuran keseluruhan elemen NumPy dalam bytes =  72
"""
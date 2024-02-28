# Tuple
# Tuple merupakan salah satu jenis dari list yang tidak dapat diubah elemennya.


# contoh deklarasi tuple
x = ("SUPPPEEEERRRR", 9, 2.5)
print(type(x))

"""
Output:
<class 'tuple'>
"""

# mengakses data dalam tuple
print(x[0])
print(x[0:2])


""" 
Output:
SUPPPEEEERRR
('SUPPPEEEERRR', 9)
"""

# data di dalam tuple tidak dapat dirubah
x[0] = "Aku ganteng"

"""
Output:
'tuple' object does not support item assignment
"""

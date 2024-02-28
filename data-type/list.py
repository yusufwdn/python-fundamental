# contoh array di python
x = [8, 2.500, "Crocodile", [1]]
print(type(x))

"""
Output: 
<class ‘list’>
"""

# mengambil data berdasarkan indeksnya
firstIndex = x[0]
lastIndex  = x[-1]

print(firstIndex)
print(lastIndex)

"""
Output:
8
[1]
"""

# metode slicing di dalam python
things = ["glass", "spoon", "plate", "fork", "table", "chair", "lamp"]

print(things[0:4:1]) # sequence[start:step:stop]
print(things[2:])    # skip 2 item pertama
print(things[:3])    # ambil 3 item pertama
"""
Output:
['glass', 'spoon', 'plate', 'fork']
['plate', 'fork', 'table', 'chair', 'lamp']
['glass', 'spoon', 'plate']
"""
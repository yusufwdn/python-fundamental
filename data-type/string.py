# simple string
string_simple = "Batavia."

print("==== Simple string ====")
print(string_simple)
print(type(string_simple))
print("")

"""
Output:
Batavia.
<class 'str'>
"""

# multi-line string 
multi_line = """Halo!
Nama aku siapa? 
Aku gak tau kamu siapa.
"""

print("==== Multiline string variable ====")
print(multi_line)

"""
Output:
Halo!
Nama aku siapa? 
Aku gak tau kamu siapa.
"""

# mengakses index dari string
print("==== Access index 'x' of a string ====")
print("first letter of string_simple value is " + string_simple[0])
print("")

"""
Output:
first letter of string_simple value is B
"""

# substring menggunakan metode indexing dan slicing
x = "Programming"
print("====  ====")
print(x[:3]) 
print(x[3:7])
print(x[7:])

"""
Output:
Pro
gram
ming
"""

# formatted string
name = "Jalaludin Scoot"
print(f"Hello, nama saya {name}")

"""
Hello, nama saya Jalaludin Scoot
"""
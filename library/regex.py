import re  # Import modul regex

pattern = '^a...s$'
text = 'abyss'
result = re.match(pattern, text)

if result:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")

"""
Output:
Pencarian berhasil.
"""
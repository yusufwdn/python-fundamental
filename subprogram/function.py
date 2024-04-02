import hello

# Fungsi Anonim (Lambda Expression)
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(25,10))

"""
Output:
250
"""

# Memanggil atau menggunakan fungsi dari modul 'hello'
persegi_panjang_external = hello.luas_persegi_panjang(8, 5)
print(persegi_panjang_external)

# Memanggil atau menggunakan fungsi internal di dalam file yang sama
persegi_panjang_internal = mencari_luas_persegi_panjang(5, 5)
print(persegi_panjang_internal)

# Keyword Argument
# Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan.
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
 
persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

# Positional Argument
# Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit.
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
 
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

# Positional-or-Keyword
# Jenis ini adalah parameter default dalam Python. Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan
 
print(greeting("Cupskyyy", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Cupskyyy"))

# Positional-Only
# Parameter ini hanya dapat dimanfaatkan menggunakan jenis argumen posisi saat pemanggilan fungsi. Parameter ini ditentukan menggunakan sintaks "/".
def penjumlahan(a, b, /):
    return a + b
 
print(penjumlahan(8, 50))

# Keyword-Only
# Parameter ini kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini. Parameter ini ditentukan dengan sintaks "*" (asterisk).
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan
 
print(greeting(pesan="Selamat sore!",nama="Cupskyyy"))

# Var-Positional
# Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args.
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total
 
print(hitung_total(1, 2, 3))


# Var-Keyword
# Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. 
# Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). 
# Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
 
print(cetak_info(nama="Cupskyyy", umur="21", pekerjaan="Senior Python Programmer"))
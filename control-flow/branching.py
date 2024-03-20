"""============ BRANCHING ============"""
"""
     Branching (percabangan) merupakan sebuah metode untuk menginstruksikan alur dari
     kode program yang sesuai dengan kondisi tertentu.
"""

# Contoh if else
ketersediaan = "Daging ayam"
if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
    Output:
    Ibu membeli dan memasak ayam
"""

# Contoh if elif dan else
nilai = 65
if nilai >= 80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai >= 70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai >= 60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")


"""
Output:
Hmm.. Anda mendapat nilai C
Ayo semangat!
"""

# Contoh if elif dan else dengan dua operand perbandingan
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik	':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

"""
Output:
Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik
Perbaiki lagi ya!
"""

# Ternary operator
# Pengkondisian dengan script yang singkat dan jelas dengan kondisi perbandingan
# value dari variabel 'lulus'.
lulus = True
print("selamat") if lulus else print("perbaiki")

"""
Output:
selamat
"""

# Ternary tuples
lulus = True
# Penjelasan tuple 'kelulusan' = (hasil_jika_kondisi_false,hasil_jika_kondisi_true)[kondisi]
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

"""
Output:
Selamat, Anda lulus!
"""
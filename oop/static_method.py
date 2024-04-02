# Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. 
# Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. 

# Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan 
# dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. 

# Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum 
# mendefinisikan fungsi atau metode.

class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""

# Pada contoh di atas, kita membuat sebuah fungsi bernama intro_mobil() yang menjadi 
# metode atau perilaku dari kelas Mobil dengan diawali oleh dekorator @staticmethod. 
"""
    Algoritma: Two Pointer

    Di sini kita akan mencoba untuk mendapatkan nilai maksimal dalam sebuah array dengan menerapkan
    algoritma Two Pointer.

    Gambaran mudahnya, kita memiliki 2 variabel, sebut saja 'left' dan 'right'. Konsep utamanya kita
    asumsikan bahwa 'left' selalu lebih besar daripada 'right'. Pada penerapan kodingnya, kita menggunakan
    looping dan if condition. Looping digunakan untuk menjabarkan seluruh nilai di array dan if condition
    digunakan untuk membandingkan nilai antara variabel 'left' dan 'right'.
"""

var_arr = [1, 7, 200, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]

    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
# Perkalian pada matriks dengan ukuran 2x2
# var_mat merupakan variabel matriks defaultnya
init_matriks = [
    [5, 0],
    [1, -2]
]

# def_mat merupakan variabel untuk menampung hasil dari perkalian, namun pada pendeklarasiannya
# diberikan nilai default matriks 2x2 dengan setiap valuenya berisi angka 0.
result_matriks = [[0 for j in range(2)] for i in range(2)]

# melakukan operasi perkalian matriks
for i in range(len(init_matriks)):
    for j in range(len(init_matriks[i])):
        # print(init_matriks[i][j])
        result_matriks[i][j] = init_matriks[i][j] * 2

print(result_matriks)
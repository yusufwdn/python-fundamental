"""============ ARRAY SEQUENTIAL ============"""
"""
    Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array.
    Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array. 

    Adapun pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari 
    elemen pada indeks terkecil hingga terbesar. Pemrosesan sekuensial lebih sering menggunakan 
    pengulangan (loop/iterasi) dalam setiap prosesnya.
"""

var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")


"""
Output:
Current element: 1, next elements: 2
Current element: 2, next elements: 3
Current element: 3, next elements: 4
Current element: 4, next elements: 5
Current element: 5, next elements: None
"""
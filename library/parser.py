import argparse

# inisiasi argparse.ArgumentParser()
parser = argparse.ArgumentParser()

# menambahkan argumen '-o', '--output' (opsional)
# perintah : python parser.py -o
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")

# menambahkan argumen required
# perintah : python parser.py -n=joker
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")

args = parser.parse_args()

# melakukan cek kondisi apakah ada argumen 'output' pada perintah yang diberikan.
if args.output:
    print("Halo, ini merupakan sebuah output dari panggildicoding.py")

print(args.nama)
# Latihan 2: Menghitung Luas dan Keliling Persegi Panjang
# Pertemuan 6 - Dasar-Dasar Pemrograman

# Trace Table:
# Skenario pengujian: panjang = 15, lebar = 8
# Langkah | Variabel panjang | Variabel lebar | Proses / Rumus | Variabel luas | Variabel keliling
# 1       | 15               | -              | input          | -             | -
# 2       | 15               | 8              | input          | -             | -
# 3       | 15               | 8              | 15 * 8         | 120           | -
# 4       | 15               | 8              | 2 * (15 + 8)   | 120           | 46

# Inisialisasi variabel input (dimensi persegi panjang dalam satuan cm)
panjang = 15
lebar = 8

# Proses komputasi rumus matematika luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil perhitungan dengan pemformatan f-string
print("Hitung Persegi Panjang:")
print(f"Panjang  : {panjang} cm")
print(f"Lebar    : {lebar} cm")
print(f"Luas     : {luas} cm2")
print(f"Keliling : {keliling} cm")

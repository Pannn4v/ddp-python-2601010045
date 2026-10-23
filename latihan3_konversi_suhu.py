# Latihan 3: Konversi Suhu
# Pertemuan 6 - Dasar-Dasar Pemrograman

# Inisialisasi variabel suhu acuan awal (dalam satuan Celsius)
suhu_celsius = 30.0

# Rumus perhitungan konversi suhu dari Celsius ke Fahrenheit dan Kelvin
fahrenheit = (9 / 5 * suhu_celsius) + 32
kelvin = suhu_celsius + 273.15

# Menampilkan hasil konversi suhu menggunakan pemformatan f-string
print("Hasil Konversi Suhu:")
print(f"Suhu Celsius  : {suhu_celsius} C")
print(f"Ke Fahrenheit : {fahrenheit} F")
print(f"Ke Kelvin     : {kelvin} K")

# Latihan 4: Menghitung Total Belanja dengan PPN 11%
# Pertemuan 6 - Dasar-Dasar Pemrograman

# Inisialisasi data transaksi pembelian barang
nama_barang = "Buku Catatan Spiral"
harga_satuan = 12000
jumlah_beli = 5
tarif_ppn = 0.11  # Besaran tarif PPN 11%

# Perhitungan komputasi finansial: subtotal, pajak PPN, dan total bayar
subtotal = harga_satuan * jumlah_beli
pajak_ppn = subtotal * tarif_ppn
total_bayar = subtotal + pajak_ppn

# Menampilkan rincian transaksi pembelian dengan pemformatan f-string
print("Rincian Pembelian:")
print(f"Barang       : {nama_barang}")
print(f"Harga Satuan : Rp {harga_satuan}")
print(f"Jumlah Beli  : {jumlah_beli}")
print(f"Subtotal     : Rp {int(subtotal)}")
print(f"PPN (11%)    : Rp {int(pajak_ppn)}")
print(f"Total Bayar  : Rp {int(total_bayar)}")

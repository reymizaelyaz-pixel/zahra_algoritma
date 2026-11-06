# ===== 1. MULAI PROGRAM =====
print("=" * 40)
print("      KASIR ELYA RESTAURANT")
print("=" * 40)
total = 0

# Data menu
menu = {
    "1": ("Nasi Goreng", 25000),
    "2": ("Mie Ayam", 15000),
    "3": ("Ayam Geprek", 20000),
    "4": ("Sate Ayam", 30000),
    "5": ("Bakso", 18000),
}

# ===== 2 - 4. TAMPILKAN MENU & PROSES PEMESANAN =====
while True:
    print("\n--- MENU MAKANAN ---")
    for kode, (nama, harga) in menu.items():
        print(f"{kode}. {nama:<12} - Rp{harga:,}".replace(",", "."))
    print("0. Selesai Memilih")

    pilihan = input("Pilih menu (0-5): ")

    # Cek apakah pilihan 0 (selesai)
    if pilihan == "0":
        break

    # Validasi pilihan
    if pilihan not in menu:
        print("Pilihan tidak valid, coba lagi!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
        continue

    nama, harga = menu[pilihan]
    subtotal = harga * jumlah
    total += subtotal
    print(f"-> {nama} x{jumlah} = Rp{subtotal:,}".replace(",", "."))

# ===== 5. HITUNG DISKON =====
if total > 200000:
    diskon = 20
else:
    diskon = 0

potongan = total * diskon / 100
total_bayar = total - potongan

# ===== 6. TAMPILKAN STRUK PEMBAYARAN =====
def rp(angka):
    return "Rp" + f"{int(angka):,}".replace(",", ".")

print("\n" + "=" * 40)
print("      STRUK - ELYA RESTAURANT")
print("=" * 40)
print(f"Total Belanja : {rp(total)}")
print(f"Diskon        : {diskon}%")
print(f"Potongan      : {rp(potongan)}")
print("-" * 40)
print(f"Total Bayar   : {rp(total_bayar)}")
print("=" * 40)
print("        Terima Kasih")

# 1. Input nama mahasiswa dan tampilkan target
nama = input("Nama : ")

# Tentukan target berdasarkan nama pakai IF - ELSE
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama tidak ditemukan! Hanya Andi, Budi, Citra.")
    exit()

print(f"Targetku {target}!")

# 2. Perulangan remedial maksimal 3 kali pakai WHILE
percobaan = 1
lulus = False

while percobaan <= 3:
    nilai = int(input(f"Nilai {percobaan} : "))

    # 3. Cek terhadap target pakai IF - ELSE
    if nilai >= target:
        lulus = True
        break
    else:
        if percobaan < 3:
            print(f"Belum lulus, remedial ke-{percobaan + 1}...")
        percobaan += 1

# 4. Tampilkan pesan akhir
print("\nOutput yang Diharapkan:")
if lulus:
    print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan!")
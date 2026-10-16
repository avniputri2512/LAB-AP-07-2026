
def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return

    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print(f"Error! Kandidat '{pilihan}' tidak terdaftar.")
        return

    rekap_suara[nama_pemilih] = pilihan
    print(f"Suara '{nama_pemilih.capitalize()}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("=======================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("=======================================")

    for kandidat in sorted(perolehan):
        print(f"   {kandidat}: {perolehan[kandidat]} suara")

    total_suara = sum(perolehan.values())
    print(f"Total suara masuk: {total_suara}")

    if len(perolehan) == 0:
        print("Belum ada kandidat.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [
        kandidat
        for kandidat, suara in perolehan.items()
        if suara == suara_tertinggi
    ]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(sorted(pemenang))}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

    print("=======================================")


kandidat_set = set()
rekap_suara = {}

print("=======================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("=======================================")

print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()

    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
            continue
        break

    daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}")

print("--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()

    if nama_pemilih == "":
        break

    if nama_pemilih.lower() in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
        continue

    print(f"Kandidat yang tersedia: {kandidat_set}")

    pilihan = input("Pilih kandidat: ").strip()

    while pilihan.capitalize() not in kandidat_set:
        print("Error! Kandidat tidak terdaftar.")
        pilihan = input("Pilih kandidat: ").strip()

    berikan_suara(
        rekap_suara,
        kandidat_set,
        nama_pemilih,
        pilihan
    )

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)

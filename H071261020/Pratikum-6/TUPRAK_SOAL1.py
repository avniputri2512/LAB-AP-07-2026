
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Buku tidak ditemukan!")
    else:
        print(f"Ditemukan {len(hasil)} buku:")

        nomor = 1

        for buku in hasil:
            print(f"{nomor}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']:g} | Stok: {buku['stok']}")
            nomor += 1


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
                return

            buku["stok"] = stok_baru
            print(
                f"Stok '{buku['judul']}' berhasil diupdate. "
                f"Stok sekarang: {buku['stok']}"
            )
            return

    print("Error! Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = None

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

        if buku_termahal is None or buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print("=" * 39)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 39)
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset:g}")

    if buku_termahal is not None:
        print(
            f"Buku termahal     : {buku_termahal['judul']} "
            f"(Rp{buku_termahal['harga']:g})"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("=" * 39)


inventaris = []

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    while True:
        pilihan = input("Pilih menu (1-5): ")

        if pilihan in ["1", "2", "3", "4", "5"]:
            break

        print("Pilihan tidak valid! Masukkan angka 1-5.")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        while True:
            try:
                harga = float(input("Harga: "))

                if harga < 0:
                    print("Harga tidak boleh negatif.")
                    continue

                break
            except ValueError:
                print("Harga harus berupa angka. Coba lagi.")

        while True:
            try:
                stok = int(input("Stok awal: "))

                if stok < 0:
                    print("Stok tidak boleh negatif.")
                    continue

                break
            except ValueError:
                print("Stok harus berupa bilangan bulat. Coba lagi.")

        tambah_buku(inventaris, judul, penulis, harga, stok)

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        while True:
            try:
                jumlah = int(
                    input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
                )
                break
            except ValueError:
                print("Jumlah harus berupa bilangan bulat. Coba lagi.")

        update_stok(inventaris, judul, jumlah)

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

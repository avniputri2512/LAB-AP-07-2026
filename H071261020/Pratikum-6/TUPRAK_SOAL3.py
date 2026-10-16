def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong!")
        return

    print("=" * 65)
    print(f"{'No':<5}{'Judul':<25}{'Artis':<20}{'Genre':<10}Durasi")
    print("=" * 65)

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60

        print(
            f"{nomor:<5}{judul:<25}{artis:<20}"
            f"{genre:<10}{menit}:{detik:02d}"
        )

        total_durasi += durasi

    print("=" * 65)
    print(
        f"Total durasi playlist: "
        f"{total_durasi // 60} menit {total_durasi % 60} detik"
    )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("=" * 45)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 45)

    print(f"Total lagu   : {len(playlist)}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    print("\nDistribusi genre:")

    if len(distribusi) == 0:
        print("  Belum ada lagu.")
    else:
        for genre, jumlah in distribusi.items():
            print(f"  {genre:<12}: # ({jumlah})")

    if len(playlist) > 0:
        lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
        lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

        durasi_panjang = lagu_terpanjang[3]
        durasi_pendek = lagu_terpendek[3]

        print(
            f"\nLagu terpanjang : {lagu_terpanjang[0]} "
            f"({durasi_panjang // 60}:{durasi_panjang % 60:02d})"
        )
        print(
            f"Lagu terpendek  : {lagu_terpendek[0]} "
            f"({durasi_pendek // 60}:{durasi_pendek % 60:02d})"
        )
    else:
        print("\nBelum ada lagu dalam playlist.")

    print("=" * 45)


playlist = []
genre_set = set()

genre_valid = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]

print("=======================================")
print("     PLAYLIST MUSIK - PLAYTUNE")
print("=======================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    while True:
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan in ["1", "2", "3", "4", "5", "6"]:
            break

        print("Pilihan tidak valid! Masukkan angka 1-6.")

    if pilihan == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()

        while True:
            genre_input = input(
                "Genre (Pop/Rock/Jazz/RnB/Dangdut): "
            ).strip()

            if genre_input.lower() in [g.lower() for g in genre_valid]:
                genre = next(
                    g for g in genre_valid
                    if g.lower() == genre_input.lower()
                )
                break

            print(
                "Genre tidak tersedia! Pilih Pop, Rock, Jazz, RnB, atau Dangdut."
            )

        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))

                if durasi <= 0:
                    print("Durasi harus berupa angka positif!")
                    continue

                break

            except ValueError:
                print("Durasi harus berupa bilangan bulat. Coba lagi.")

        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Playlist masih kosong, belum ada genre tersedia.")
            continue

        print(f"Genre tersedia: {genre_set}")

        while True:
            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            ).strip()

            genre_cocok = next(
                (g for g in genre_set if g.lower() == genre_target.lower()),
                None
            )

            if genre_cocok is not None:
                break

            print("Genre tidak tersedia! Silakan masukkan ulang.")

        hasil = filter_genre(playlist, genre_cocok)

        print(f"\nLagu bergenre '{genre_cocok}':")

        if len(hasil) == 0:
            print("Tidak ada lagu dengan genre tersebut.")
        else:
            for nomor, lagu in enumerate(hasil, start=1):
                judul, artis, genre, durasi = lagu
                print(
                    f"  {nomor}. {judul} - {artis} "
                    f"({durasi // 60}:{durasi % 60:02d})"
                )

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong!")
            continue

        tampilkan_playlist(playlist)

        while True:
            try:
                nomor = int(
                    input("Masukkan nomor lagu yang ingin dihapus: ")
                )

                if nomor < 1 or nomor > len(playlist):
                    print("Nomor lagu tidak valid! Coba lagi.")
                    continue

                break

            except ValueError:
                print("Nomor harus berupa bilangan bulat. Coba lagi.")

        hapus_lagu(playlist, nomor)

        genre_set = {lagu[2] for lagu in playlist}

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

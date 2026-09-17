tujuan = input("Masukkan tujuan (Pantai/Penggunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu(Pagi/Malam):").capitalize()
Tipe_Pengunjung = input("Masukkan tipe pengunjung (Dewasa/Anak-anak):").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")
        
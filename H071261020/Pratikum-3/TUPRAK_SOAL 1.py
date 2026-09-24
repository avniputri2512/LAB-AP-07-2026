print("---Rekapitulasi Transaksi Dins Store--- ")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")


while True:
    try:
        jumlah_item = int(input("Masukkan jumlah item: "))

        if jumlah_item == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break
        if jumlah_item < 0:
            print("Jumlah tidak boleh negatif")
            continue
        if jumlah_item > 100:
            print("Maksimal 100 item per transaksi!")
            continue
        print(f"Transaksi {jumlah_item} item berhasil!")

    except ValueError:
        print("Input harus berupa angka bulat!")

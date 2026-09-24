while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))

        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
        else:
            break

    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

sisa_kursi = N
total_pendapatan = 0

print("--- Sistem Reservasi PO BUS Dimulai ---")

while sisa_kursi > 0:
    print("Sisa kursi:", sisa_kursi)

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    elif umur <= 5:
        kategori = "Balita"
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")

    elif umur <= 12:
        kategori = "Anak"
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000")

    else:
        kategori = "Dewasa"
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000")

    sisa_kursi -= 1
    total_pendapatan += harga

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)
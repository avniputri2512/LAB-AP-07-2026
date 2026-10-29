import os
import random
from datetime import datetime


FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "trx_history.txt"
LEBAR = 60
GARIS = "=" * LEBAR
LEBAR_LABEL = 25


def garis():
    print(GARIS)


def judul(teks):
    print(teks.center(LEBAR).rstrip())


def tanya(label, tipe="teks", minimal=1):
    while True:
        teks = input(f"{label:<{LEBAR_LABEL}}: ").strip()

        if tipe == "angka":
            if teks.isdigit() and int(teks) >= minimal:
                return int(teks)
            print(f"Input tidak valid, masukkan angka bulat >= {minimal}.")
        elif tipe == "yt":
            if teks.lower() in ("y", "t"):
                return teks.lower()
            print("Input tidak valid, masukkan y atau t.")
        else:
            if teks:
                return teks
            print("Input tidak boleh kosong.")


def rupiah(angka):
    return f"Rp. {angka:,}".replace(",", ".")


# SOAL 1

def buat_id_transaksi(nama_kasir, waktu):
    inisial = "".join(kata[:3] for kata in nama_kasir.split()).upper()

    while True:
        id_trx = (
            f"{inisial}{waktu.strftime('%y%m%d')}"      #strftime digunakan untuk mengubah nilai tanggal dan waktu menjadi teks dengan format tertentu.
            f"{waktu.strftime('%H%M')}{random.randint(100, 999)}"
        )
        path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")

        if not os.path.exists(path):
            return id_trx


def buat_isi_invoice(id_trx, waktu, nama_kasir, daftar_produk, total):
    sep = "=" * 70
    baris = [
        sep,
        "INVOICE".center(70),
        sep,
        f"ID Transaksi : {id_trx}",
        f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Kasir        : {nama_kasir}",
        sep,
        f"{'No':<4}{'Produk':<25}{'Harga':>12}{'Qty':>6}{'Subtotal':>15}",
        "-" * 70,
    ]

    for no, p in enumerate(daftar_produk, start=1):
        baris.append(
            f"{no:<4}{p['nama'][:24]:<25}"
            f"{rupiah(p['harga']):>12}{p['jumlah']:>6}"
            f"{rupiah(p['subtotal']):>15}"
        )

    baris += [
        "-" * 70,
        f"{'TOTAL':<47}{rupiah(total):>23}",
        sep
    ]

    return "\n".join(baris) + "\n"


def transaksi_baru(nama_kasir):
    garis()
    daftar_produk = []

    while True:
        nama = tanya("Masukkan nama produk")
        harga = tanya("Masukkan harga produk", "angka", minimal=0)
        jumlah = tanya("Masukkan jumlah produk", "angka", minimal=1)

        daftar_produk.append({
            "nama": nama,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": harga * jumlah
        })

        garis()
        lagi = tanya("Tambah produk? (y/t)", "yt")
        garis()

        if lagi == "t":
            break

    waktu = datetime.now()
    total = sum(p["subtotal"] for p in daftar_produk)

    os.makedirs(FOLDER_INVOICE, exist_ok=True)


    while True:
        id_trx = buat_id_transaksi(nama_kasir, waktu)
        path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")

        try:
            with open(path, "x", encoding="utf-8") as f:
                f.write(
                    buat_isi_invoice(
                        id_trx, waktu, nama_kasir, daftar_produk, total
                    )
                )
            break
        except FileExistsError:
            continue

    catat_riwayat(waktu, id_trx, total)

    judul("TRANSAKSI BERHASIL")
    print(f"ID Transaksi : {id_trx}")
    print(f"Total        : {rupiah(total)}")
    garis()


# SOAL 2

def cari_transaksi():
    garis()
    id_trx = tanya("Masukkan ID transaksi")

    if id_trx.lower().endswith(".txt"):
        id_trx = id_trx[:-4]

    garis()
    path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")

    if not os.path.isfile(path):
        judul("TRANSAKSI TIDAK DITEMUKAN")
        garis()
        return

    with open(path, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    garis()


# SOAL 3

def catat_riwayat(waktu, id_trx, total):
    sep = "=" * 90
    header = (
        f"| {'Waktu':^21} | {'ID Transaksi':^20} | "
        f"{'Nominal Transaksi':^20} |"
    )
    data = (
        f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<21} | "
        f"{id_trx:<20} | {rupiah(total):>20} |"
    )

    if os.path.isfile(FILE_RIWAYAT):
        with open(FILE_RIWAYAT, "r", encoding="utf-8") as f:
            baris = f.read().splitlines()

        if not baris:
            baris = [sep, header, sep]
        elif baris[-1] == sep:
            baris.pop()
    else:
        baris = [sep, header, sep]

    baris.append(data)
    baris.append(sep)

    with open(FILE_RIWAYAT, "w", encoding="utf-8") as f:
        f.write("\n".join(baris) + "\n")


# MENU UTAMA

def main():
    os.makedirs(FOLDER_INVOICE, exist_ok=True)

    garis()
    judul("SELAMAT DATANG")
    garis()

    nama_kasir = tanya("Masukkan nama kasir")
    garis()

    while True:
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        garis()

        pilihan = tanya("Masukkan opsi pilihan")

        if pilihan == "1":
            transaksi_baru(nama_kasir)
        elif pilihan == "2":
            cari_transaksi()
        elif pilihan == "3":
            garis()
            judul("TERIMA KASIH")
            garis()
            break
        else:
            garis()
            judul("OPSI TIDAK VALID")
            garis()


if __name__ == "__main__":     #kapan fungsi dijalankan
    main()

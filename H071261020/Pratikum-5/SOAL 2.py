def cek_kata(teks, kata):
    indeks = []
    start = 0

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    while True:
        i = teks_kecil.find(kata_kecil, start)

        if i == -1:
            break

        indeks.append(i)
        start = i + 1

    return indeks


def cek_batas(teks, i, panjang):
    if i > 0:
        sebelum = teks[i - 1].lower()
        if 'a' <= sebelum <= 'z':
            return False

    if i + panjang < len(teks):
        sesudah = teks[i + panjang].lower()
        if 'a' <= sesudah <= 'z':
            return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_awal = []
    jumlah_tersensor = 0
    hasil = ""
    posisi = 0

    indeks = cek_kata(teks, kata)

    for i in indeks:
        if i < posisi:
            continue

        if cek_batas(teks, i, len(kata)):
            hasil += teks[posisi:i]
            hasil += simbol * len(kata)

            posisi = i + len(kata)
            indeks_awal.append(i)
            jumlah_tersensor += 1

    hasil += teks[posisi:]

    return hasil, jumlah_tersensor, indeks_awal


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)

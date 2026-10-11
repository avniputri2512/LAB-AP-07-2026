def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in teks:
        if karakter.lower() in alfabet:
            hasil += karakter.lower()

    return hasil


def cek_palindrome(teks):
    teks_balik = "".join(reversed(teks))

    if teks == teks_balik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)


def inti_palindrome(teks):
    teks = bersihkan_teks(teks)

    palindrome_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            substring = teks[i:j]
            hasil_cek = cek_palindrome(substring)

            if hasil_cek[0]:
                if len(substring) > len(palindrome_terpanjang):
                    palindrome_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrome_terpanjang,
        "panjang": len(palindrome_terpanjang),
        "indeks_awal": indeks_awal
    }


teks = input("Masukkan teks prasasti: ")
print("Teks Bersih:", bersihkan_teks(teks))
print("Output Terharap:", inti_palindrome(teks))
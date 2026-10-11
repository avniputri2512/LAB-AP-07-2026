ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:
        return ch
    huruf_baru = ALFABET[(posisi + k) % 26]
    if ch.isupper():
        return huruf_baru.upper()
    return huruf_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for kunci in range(26):
        pesan = mesin_dekripsi(sandi, kunci)
        if pesan.lower().find(kata_kunci.lower())             != -1:
            hasil.append((kunci, pesan))
    return hasil

sandi = input("Masukan pesan tersandi: ")
target = input("Masukan kata kunci target: ")
print("Output Deskripsi:", retas_sandi(sandi, target))
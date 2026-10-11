def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi di posisi manapun.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau memiliki titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")

    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (domain.endswith(".com") or
            domain.endswith(".id") or
            domain.endswith(".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id.")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return

    panjang = max(len(email) for email in daftar_email_valid)

    print(karakter_border * (panjang + 4))

    for email in daftar_email_valid:
        print(karakter_border + " " + email.ljust(panjang) + " " + karakter_border)

    print(karakter_border * (panjang + 4))


print("--- Sistem Pencatatan email valid ---")

karakter_border = input("Masukkan border dengan karakter bebas: ")

daftar_email_valid = []

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    if len(error) > 0:
        print(">> Email DITOLAK karena:")

        for pesan in error:
            print("   -", pesan)

    elif email in daftar_email_valid:
        print(">> Email DITOLAK karena:")
        print("   - Email sudah terdaftar (Duplikat).")

    else:
        daftar_email_valid.append(email)
        print(">> Email VALID!")


print()
print("--- HASIL EMAIL VALID ---")

cetak_daftar(daftar_email_valid, karakter_border)
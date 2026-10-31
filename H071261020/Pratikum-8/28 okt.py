import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim)

def validasi_email(email):
    return re.fullmatch(r"\w+@\w+\.\w+", email)

def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}", telepon)

print("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM: ")
email = input("Masukkan email: ")
telepon = input("Masukkan nomor telepon: ")

print("\n--- Hasil Validasi ---")

valid = True

if validasi_nim(nim):
    print("NIM valid.")
else:
    print("Format NIM tidak valid!")
    valid = False

if validasi_email(email):
    print("Email valid.")
else:
    print("Format email tidak valid!")
    valid = False

if validasi_telepon(telepon):
    print("Nomor telepon valid.")
else:
    print("Nomor telepon tidak valid!")
    valid = False

if valid:
    print("Data mahasiswa berhasil diverifikasi!")
else:
    print("Data mahasiswa gagal diverifikasi!")




import re

username_valid = []

def validasi(username):
    pola = r'^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    return re.match(pola, username) is not None

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

while True:
    username = input("\nMasukkan username: ")

    if username.upper() == "SELESAI":
        break

    if validasi(username):
        print("Username tersedia.")
        username_valid.append(username)
    else:
        print("Username tidak valid!")

print("\n=== Rekapitulasi ===")
print("Username valid:")

for i, username in enumerate(username_valid, 1):
    print(f"{i}. {username}")


print("\nJumlah username valid:", len(username_valid))

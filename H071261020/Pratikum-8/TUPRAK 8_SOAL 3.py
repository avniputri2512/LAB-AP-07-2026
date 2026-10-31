import re

data_telepon = []
nomor_valid = []

print("=== Pembersihan Data Nomor Telepon ===")

jumlah = int(input("\nMasukkan jumlah data: "))

print("\n--- Hasil Pembersihan ---")

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    data_telepon.append(nomor)

print("\n--- Hasil Pembersihan ---")

for i in range(jumlah):
    nomor = data_telepon[i]
    bersih = re.sub(r'[\s-]', '', nomor)

    if re.fullmatch(r'\d{10,13}', bersih):
        status = "Valid"
        nomor_valid.append(bersih)
    else:
        status = "Tidak valid"

    print(f"\nData {i + 1}:")
    print("Sebelum :", nomor)
    print("Sesudah :", bersih)
    print("Status  :", status)

print("\nJumlah nomor valid:", len(nomor_valid))


































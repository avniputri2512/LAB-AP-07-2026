jarak=int(input("Masukkan jarak pengiriman (km): "))
express=input("Layanan express? (ya/tidak):").lower()
if jarak < 5:
    tarif = 10000
elif 5 <= jarak <= 20:
    tarif = 20000
else:
    tarif = 35000
harga_total = int(tarif + 15000) if express == "ya" else tarif
print(f"total tarif pengiriman: Rp {harga_total}")
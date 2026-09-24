print("---Setup Denah Bioskop NontonYuk---")

while True:
    try:
        N = int(input("Masukkan jumlah baris: "))

        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break

    except ValueError :
        print("Input baris harus berupa angka!")


while True:
    try:
        M = int(input("Masukkan jumlah kursi per baris: "))

        if M <= 0:
            print("Jumlah kursi per baris harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input jumlah kursi per baris harus berupa angka!")


print("---Daftar Kursi Tersedia---")

for baris in range(1, N + 1):
    for kursi in range(1, M + 1):

        if kursi == 13:
            continue

        if baris == 1:
            if kursi % 2 == 0:
                continue
        else:
            print(f"Baris {baris} - Kursi {kursi}")
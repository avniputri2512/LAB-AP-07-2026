nilai_tes = int(input("Masukkan nilai tes:"))

if nilai_tes >= 80:
    print("Lolos ke tahap wawancara")
else:
    pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun):"))
    if nilai_tes >= 65 and pengalaman_kerja >= 2:
        print("Lolos bersyarat")
    else:
        print("Tidak lolos ")
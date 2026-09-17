presentase = int(input("Masukkan presentase: ") ) 

if presentase < 0:
    print("tidak valid")
elif 0 <= presentase <= 10:
    print("level aman")
elif 11 <= presentase <= 40:
    print("level sedang")
elif 41 <= presentase <= 70:
    print("level pedas")
elif 71 <= presentase <= 100:
    print("level ekstrem")
else :
    print("tidak ada level")
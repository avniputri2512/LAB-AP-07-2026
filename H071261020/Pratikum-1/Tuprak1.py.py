menu  = ["Kopi susu","Matcha latte","Americano"]
harga = [18000,22000,15000]
jumlah =[4,3,5]

#Mengitung sub total dari masing-masing kopi
sub_Kopi      = harga[0] * jumlah[0]
sub_Matcha    = harga[1] * jumlah[1]
sub_Americano = harga[2] * jumlah[2]

#memasukkan sub total ke dalam list
subtotal_pendapatan = [sub_Kopi,sub_Matcha,sub_Americano]

#Menghitung total pendapatan dan pendapatan bersih
total_seluruh = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#menghitung jumlah kopi yang terjual
total_kopi = sum(jumlah)

target_tercapai = total_seluruh > 200000 and total_kopi > 10

#hasil
print("subtotal Kopi susu :",sub_Kopi )
print("subtotal Matcha latte :",sub_Matcha )
print("subtotal Americano :",sub_Americano)
print("Pendapatan Bersih:",pendapatan_bersih)
print("Target Tercapai:",target_tercapai)


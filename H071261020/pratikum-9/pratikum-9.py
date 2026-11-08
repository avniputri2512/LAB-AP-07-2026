class Pemain:
    def __init__(self,nama,id_pemain,role,nilai_kill,nilai_assist,nilai_objective):
        self.nama = nama
        self.id_pemain= id_pemain
        self.role= role
        self.nilai_kill = nilai_kill
        self.nilai_assist= nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return ('unggul')
        else:
            return('perlu evaluasi!')

    def tampilkan_data(self):
        print(self.nama,self.id_pemain,self.role)

daftar_pemain= []

print('===SISITEM PENILAIAN PEFORMA PEMAIN===')

while True:
    try:
        jumlah = int(input("Masukkan jumlah pemain: "))
        if jumlah > 0:
            break
        print('jumlah harus lebih dari 0!')
    except ValueError:
        print('Masukkan angka dengan benar!')

for i in range(jumlah):
    print('Data pemain ke',i+1)

    nama = input("masukkan nama:")
    id_pemain = input('Masukkan id pemain:')
    role = input("masukkan role pemain:")

    while True:
        try:
            kill = int(input("Masukkan nilai kill: "))
            if kill >= 0:
                break
            print('jumlah tidak boleh negatif!')
        except ValueError:
            print('Masukkan angka dengan benar!')
    while True:
        try:
            assist = int(input("Masukkan nilai assist: "))
            if assist >= 0:
                break
            print('jumlah tidak boleh negatif!')
        except ValueError:
            print('Masukkan angka dengan benar!')
    while True:
        try:
            objective = int(input("Masukkan nilai objective: "))
            if objective >= 0:
                break
            print('jumlah tidak boleh negatif!')
        except ValueError:
            print('Masukkan angka dengan benar!')

    pemain = Pemain(nama,id_pemain,role,kill,assist,objective)
    daftar_pemain.append(pemain) 

print('=== REKAPITULASI PERFORMA PEMAIN ===')

print("-" * 85)
print(f"| {'No':<3} | {'Nama':<15} | {'ID Pemain':<15} | {'Role':<12} | {'Skor Akhir':<12} | {'Status':<15} |")
print("-" * 85)

for i, pemain in enumerate(daftar_pemain, 1):
    print(f"| {i:<3} | {pemain.nama:<15} | {pemain.id_pemain:<15} | {pemain.role:<12} | {pemain.hitung_skor_akhir():<12.2f} | {pemain.status_performa():<15} |")

print("-" * 85)


        


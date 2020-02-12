
# 1. Jika user memasukkan qty lebih dr stock, 
#       minta user utk input ulang sampai tidak melebihi stock
# 2. Minta user input sejumlah uang
#       Jika uangnya kurang, munculkan pesan kurangnya berapa kemudian minta pembeli input lagi
#    Jika uangnya pas / lebih, maka muncul "Terima kasih"

jumlahApel = 5
jumlahAnggur = 7
jumlahJeruk = 8

hargaApel = 10000
hargaAnggur = 15000
hargaJeruk = 20000

beliApel = int(input("Masukkan jumlah apel yang mau dibeli: "))

while beliApel > jumlahApel:
    print(f"Ada kesalahan input, maksimal jumlah apel yang dapat dibeli: {jumlahApel}")
    beliApel = int(input("Silakan input jumlah lain apel yang mau dibeli: "))
    break
if beliApel <= jumlahApel:
    totalbeliApel = int(beliApel * hargaApel)
else:
    totalbeliApel = int(beliApel * hargaApel)

# cara lain, bisa juga pakai variable baru misal askAgain
# askAgain = TRUE
# while askAgain:
# beliApel = int(input("Masukkan jumlah apel yang mau dibeli: "))
# if jumlahApel < beliApel:
#     totalbeliApel = int(beliApel * hargaApel)
# else:
#     askAgain = FALSE



beliAnggur = int(input("Masukkan jumlah anggur yang mau dibeli: "))

while beliAnggur > jumlahAnggur:
    print(f"Ada kesalahan input, maksimal jumlah anggur yang dapat dibeli: {jumlahAnggur}")
    beliAnggur = int(input("Silakan input jumlah anggur yang mau dibeli: "))
    break
if beliAnggur <= jumlahAnggur:
    totalbeliAnggur = int(beliAnggur * hargaAnggur)
else:
    totalbeliAnggur = int(beliAnggur * hargaAnggur)

beliJeruk = int(input("Masukkan jumlah jeruk yang mau dibeli: "))

while beliJeruk > jumlahJeruk:
    print(f"Ada kesalahan input, maksimal jumlah jeruk yang dapat dibeli: {jumlahJeruk}")
    beliJeruk = int(input("Silakan input jumlah jeruk yang mau dibeli: "))
    break
if beliJeruk <= jumlahJeruk:
    totalbeliJeruk = int(beliJeruk * hargaJeruk)
else:
    totalbeliJeruk = int(beliJeruk * hargaJeruk)

totalBelanja = totalbeliApel + totalbeliAnggur + totalbeliJeruk

print("------------------------------------------------------------")
print(f"Total belanja buah apel @10000 x {beliApel} = Rp {totalbeliApel}")
print(f"Total belanja buah anggur @15000 x {beliAnggur} = Rp {totalbeliAnggur}")
print(f"Total belanja buah jeruk @20000 x {beliJeruk} = Rp {totalbeliJeruk}")
print("------------------------------------------------------------")

# tampilkan jumlah belanja dengan detail hitung totalnya
print(f"Maka total belanja Anda: Rp {totalBelanja}")

moneyAgain = True
# User input uang
while moneyAgain:
    userMoney = int(input("Masukkan jumlah Anda: Rp " ))

# cari selisih uang user dgn total belanja
    margin = userMoney - totalBelanja

    if userMoney < totalBelanja: 
    userMoney
    # if inputUanglagi < kurangBayar:
    #     inputUanglagi= int(input("Silakan masukkan uang Anda lagi: Rp "))
    # elif inputUanglagi > kurangBayar:
    #     kembaliannya = inputUanglagi - kurangBayar
    #     print(f"Kembalian Anda : Rp {kembaliannya}")
elif inputUang > totalBelanja:
    kembalian = inputUang - totalBelanja
    print(f"Kembalian Anda : Rp {kembalian}")
else:
    inputUang = totalBelanja
    print(f"Uang yang Anda masukkan pas.")

print("Terima kasih telah berbelanja!")

print("------------------------------------------------------------")
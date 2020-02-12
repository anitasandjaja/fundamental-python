# angka = int(input("Masukkan angka: "))
# if angka % 2 == 0:
#     print(f"Angka  {angka} tergolong bilangan GENAP")
# else:
#     print(f"Angka {angka} tergolong bilangan GANJIL")


##########################

# mass = int(input('Masukkan berat badan (kg) : '))
# height = int(input('Masukkan tinggi badan (cm) : '))
# imt = mass / ((height/100) ** 2)

# if imt < 18.5:
#     print('Massa', mass, 'kg & tinggi', height, 'cm')
#     print('IMT =', imt, ': BB Anda masih kurang!')
# elif imt >= 18.5 and imt <= 24.9:
#     print('Massa', mass, 'kg & tinggi', height, 'cm')
#     print('IMT =', imt, ': BB Anda sudah ideal!')
# elif imt >= 25.0 and imt <= 29.9:
#     print('Massa', mass, 'kg & tinggi', height, 'cm')
#     print('IMT =', imt, ': BB Anda berlebih, ayo mulai olahraga!')
# elif imt >= 30.0 and imt <= 39.9:
#     print('Massa', mass, 'kg & tinggi', height, 'cm')
#     print('IMT =', imt, ': BB Anda sangat berlebih! Atur pola makan dan rajin berolahraga!!')
# else:
#     print('Massa', mass, 'kg & tinggi', height, 'cm')
#     print('IMT =', imt, ': BB Obesitas! Segera konsul ke Ade Rai!')


###################### BELANJA BUAH ##############################

jumlahApel = 5
jumlahAnggur = 7
jumlahJeruk = 8

hargaApel = 10000
hargaAnggur = 15000
hargaJeruk = 20000

# meminta quantity yg mau dibeli dari setiap buah
beliApel = int(input("Masukkan jumlah apel yang mau dibeli: "))
if beliApel > jumlahApel:
    print(f"Ada kesalahan input, stok buah apel ada {jumlahApel} buah, silakan input jumlah lain")
    beliApel = 0

beliAnggur = int(input("Masukkan jumlah anggur yang mau dibeli: "))

if beliAnggur > jumlahAnggur:
    print(f"Ada kesalahan input, stok buah anggur ada {jumlahAnggur} buah")
    beliAnggur = 0

beliJeruk = int(input("Masukkan jumlah jeruk yang mau dibeli: "))

if beliJeruk > jumlahJeruk:
    print(f"Ada kesalahan input, stok buah jeruk ada {jumlahJeruk} buah")
    beliJeruk = 0

totalbelanjaApel = beliApel*hargaApel
totalbelanjaAnggur = beliAnggur * hargaAnggur
totalbelanjaJeruk = beliJeruk*hargaJeruk

totalBelanja = totalbelanjaApel + totalbelanjaAnggur + totalbelanjaJeruk

print("------------------------------------------------------------")
print("------------------------------------------------------------")
print(f"Total belanja buah apel @10000 x {beliApel} = Rp {totalbelanjaApel}")
print(f"Total belanja buah anggur @15000 x {beliAnggur} = Rp {totalbelanjaAnggur}")
print(f"Total belanja buah jeruk @20000 x {beliJeruk} = Rp {totalbelanjaJeruk}")
print("------------------------------------------------------------")
print("------------------------------------------------------------")

# tampilkan jumlah belanja dengan detail hitung totalnya
print(f"Maka total belanja Anda: Rp {totalBelanja}")
print(f"Terima kasih telah berbelanja!")
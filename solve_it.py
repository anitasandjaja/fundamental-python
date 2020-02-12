# solve it_1

# import math
# x = 4
# y = 3
# z = 2

# w = (( x + y * z ) / ( x*y ))**z
# print (w)

#### OR

# v = ( x + y * z ) / ( x*y )
# result = math.pow(v,z)
# print(result)


# solve it_2

# x = input("Silakan masukkan angka berapapun: ") #meminta input dari user n disimpan di variable, 
# #input dr user akan selalu string

# x = int(x)  # ubah input dari user menjadi integer
# kuadrat = x**2 # hitung kuadrat input dr user
# kuadrat = int(kuadrat)
# print(f"Hasil kuadrat dari {x} adalah: {kuadrat}")  # hasil kuadrat ditampilkan


# solve it 3

# 1 tahun = 360 hari, 1 bulan = 30 hari, 1 minggu 7 hari


# # Tentukan banyaknya hari
# days = 485

# # Tentukan jumlah tahun
# year = int(days / 360)
# # Sisa hari setelah diambil sekian tahun
# days = days % 360

# # Tentukan jumlah bulan
# month = int(days / 30)
# # Sisa hari setelah diambil sekian bulan
# days = days % 30

# # Tentukan jumlah minggu
# week = int(days / 7)

# Sisa hari setelah diambil sekian minggu
# days = days % 7
# print("Maka 485 hari terdiri dari:")
# print(f"{year} tahun")
# print(f"{month} bulan")
# print(f"{week} minggu")
# print(f"{days} hari")


############################
# number of days in terms of Years, Month, Weeks and Days 
# DAYS_IN_WEEK = 7
# DAYS_IN_MONTH = 30
  
# # Function to find year, week, days  
# def find( number_of_days ): 
  
#     # Assume that years is of 360 days 
#     year = int(number_of_days / 360)
#     month = int((number_of_days % 360) / DAYS_IN_MONTH)
#     week = int((number_of_days % 7) / DAYS_IN_WEEK) 
#     days = (number_of_days % 360) % DAYS_IN_MONTH 
      
#     print("years = ",year,
#           "\nmonth =", month,
#           "\nweeks = ",week, 
#           "\ndays = ",days) 
      
# number_of_days = 485
# find(number_of_days) 



#solve it 4

# andi/budi = 0.4
# andi + budi = 49
# andi = 49 - budi
# (49-budi) / budi = 0.4
# 49 - budi = 0.4*budi
# 49 = 1.4*budi
# budi = 49/1.4
# budi = 35
# andi = 49 - 35
# andi = 14 

jumlah = 49
rasio = 0.4

andi = jumlah / (rasio + 1)
budi = jumlah - andi

print(andi)
print(budi)

# usia 2 th lagi

andi = andi + 2
budi = budi + 2

print(andi)
print(budi)


# solve it 5

# x = input("Silakan masukan kalimat: ")
# y = input ("Karakter apa yang ingin diketahui jumlahnya: ")
# result = x.count(y)
# print(f"Pada \"{x}\" terdapat karakter \"{y}\" sebanyak {result} buah") 


# # solve it 6

v1 = 60
v2 = 40
s = 120
jam = 9

t = s / (v1+v2)
s1 = t*v1
s2 = t*v2

print (f"Waktu yang diperlukan {t} jam")
print (f"Jarak A ke titik C = {s1} km")
print (f"Jarak B ke titik C = {s2} km")

totalJam = int(t+jam)
minutes = int(t*60)%60

print(f"Maka akan bertemu di pukul {totalJam} lewat {minutes} menit")

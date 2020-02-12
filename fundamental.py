# Untuk menampilkan teks (komentar)
#print('My first code')

# Variable: untuk menyimpan sebuah data
# Tidak bisa diawali dengan angka
# string, tipe data yg menyimpan teks = 'Vinales'
# number, float: desimal (0.25, 3.14), integer: bulat (3, 5, 6)
# penulisan variable dengan camelCase
# firstName = 'Vinales'
# lastName = 'John'
# age = 32

# Function type digunakan untuk mengetahui tipe data dari sebuah variable
# result = type(age)
# print(result)
# print(type(age))

# function input digunakan untuk menerima inputan user
# name = input("Siapa Nama Anda : ")
# day = input("Hari apakah saat ini : ")

# print('Nama saya adalah  ' + name)
# print('Hari ini adalah hari ' + day)

## S H O R T C U T ##
# Duplicate code : SHIFT + ALT + DOWN ARROW
# Untuk membersihkan terminal : CTRL + L
# Membuat komentar : CTRL + /
# Membuka / menutup terminal : CTRL + J
# Tekan Alt + click kursor

#syntax print untuk menampilkan  teks 
# print("first code asddddhgsd1233")

#untuk nampilin / nutup terminal Ctrl+J
#Ctrl+L utk clear terminal

#variable utk menyimpan data
#tidak bisa diawali dengan angka

# firstName = 'anita'
# lastName = 'sandjaja'
# age = 25
# print(firstName)
# print(lastName)
# print(age) 

# firstName = input("Nama depan: ")
# lastName = input("Nama belakang: ")
# namaLengkap = firstName + " " +lastName
# hobi = input("Hobi: ")

# print('Nama lengkap saya '+ namaLengkap +' dan hobi saya '+ hobi)

## ARITHMATIC ##

# function int akan mengubah string menjadi integer
# hasil = numOne + int(numThree)
# print(hasil)
# numOne = 10
# numTwo = 5
# numThree = "7"
# result = numOne + numTwo

# numOneString = str(numOne) #numOne = 10-> jadi numOneString = "10"
# numTwoString = str(numTwo) #numTwo = 5-> jadi numTwoString = "5"
# resultString = str(result) #result = 15-> jadi resultString = "15"

# result = numOne + numTwo
# print(numOneString + " + " + numTwoString + " = " + str(result))

# result = numOne - numTwo
# print(numOneString + " - " + numTwoString + " = " + str(result))

# result = numOne * numTwo
# print(numOneString + " * " + numTwoString + " = " + str(result))

# result = numOne / numTwo
# print(numOneString + " / " + numTwoString + " = " + str(result))

# result = numOne % numTwo
# print(numOneString + " % " + numTwoString + " = " + str(result))

# result = numOne ** numTwo
# print(numOneString + " ** " + numTwoString + " = " + str(result))


# ageJohn = 47
# ageKobe = 41

# ageJohn = ageJohn + 3
# ageJohn += 3

# ageKobe = ageKobe -1
# ageKobe -= 1
# print (ageJohn)
# print (ageKobe)


#module Math
import math

# mengabsolute sebuah nilai tanpa mengubah tipe datanya
print(abs(-13))

# mengabsolutekan sebuah nilai kemudian diubah menjadi tipe data float
print(math.fabs(-4))

#pangkat
print(math.pow(8,2))
print(math.pow(8,3))

# akar
print(math.sqrt(64))

# round - pembulatan
print(round(4.7))
print(round(4.12))

# floor utk pembulatan ke bawah
print(math.floor(4.7))

# ceil utk pembulatan ke atas
print(math.ceil (4.12))


# string

x = 'Halo Dunia ku yang cerah'

# print(len(x)) # menghitung banyak karakter pada string
# print(x.index('Dunia')) # mengetahui letak suatu kata)
# kalau diganti jadi 'dunia' maka hasilnya substring not found, case sensitive

# print(x.split())
# print(x.split(" "))

# mengubah menjadi hufur kecil
# print(x.lower())

# mengubah menjadi huruf besar
# print(x.upper())

#mengubah huruf besar utk huruf pertama kalimat
# print(x.capitalize())

# print("hello, i'am ironman")
# print('hello, i\'am ironman')
# print('You are "crazy"')
# print("You are \"crazy\" ")

# \n untuk membuat baris baru, enter, new line
print("Hello, i'am ironman" + "\n" +"and i'am \"crazy\"")

print(
    "Hello, i'am ironman" + "\n" + 
    "and i'am \"crazy\""
)


############################################

# Logic, operator, if else statement

# Hujan

# if hujan:
#     pakai payung
# else:
#     tidak pakai payung



# Umur

# if lebih dari 18:
#     boleh masuk bioskop
# elif 15 - 17:
#     boleh masuk tp, dgn org tua
# else:
#     tidak boleh masuk bioskop


# Tipe Data: 
# BOOLEAN (TRUE, FALSE)

# Number one

# Buatlah sebuah function yang menerima sebuah kata
# Reverse huruf setiap kata

# Contoh:
#   Hello my friend --> olleH ym dneirf
#   abc de efg --> cba ed gfe
# nama function wordRev

# def wordRev(word):
#     word = word.split()
#     reversed_word = [w[::-1] for w in word]
#     word = " ".join(reversed_word)
#     print(word)

# wordRev("Hello my friend")


# Number two
# Buat function yang menerima list of number
# Jumlahkan semua angka, kecuali angka yang ada di antara 0 - 1

# nama function sum01
# [2, 4, 0, 1, 11] --> 17
# [7, 0, 3, 1, 7, 9] --> 23
# [5, 0, 3, 2, 1] --> 5

def sum01(num):
    # Temukan index angka 0 dan 1
    # Untuk index angka 1 dijumlah angka 1 
    nol = num.index(0)
    satu = num.index(1) + 1

    # Delete data dari index angka 0 hingga index angka 1
    del num[nol:satu]
    
    # Sisa angka pada list dijumlahkan
    result = sum(num)
    print(result)

sum01([2, 4, 0, 1, 11])
sum01([7, 0, 3, 1, 7, 9])
sum01([5, 0, 3, 2, 1])
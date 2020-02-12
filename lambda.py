# def times2(num):
#     return num * 2

# result = times2(4) # 2

# Lambda #
# Biasa digunakan sebagai callback function

# lambda num: num * 2

# MAP #
# Digunakan untuk merubah bentuk data
# Menerima dua parameter , function dan list
# function yang memiliki istilah 'callback function'
# function ini harus menerima satu buah parameter
# function tersebut harus me return sesuatu
# return mapobject, untuk mendapatkan listnya harus
# dimasukkan ke dalam function list()

# with function
# def times2(num):
#     return num * 2

# numList = [1, 2, 3 ,4 , 5]

# mapObj = map(times2, numList)
# result = list(mapObj)

# print (numList)
# print(result)

# with lambda

# mapObj = map(lambda num: num * 2, numList)
# result = list(mapObj)

# print(result)


# FILTER #
# Digunakan untuk menyaring data
# Menerima dua parameter, function dan list
# function yang memiliki istilah 'callback function'
# function ini harus menerima satu buah parameter
# function tersebut harus me-return hasil berupa boolean (True , False)
# return filterobject, untuk mendapatkan listnya harus
# dimasukkan ke dalam function list()

# with function
# def even(num):
#     return num % 2 == 0

# numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]

# evenList = list(filter(even, numList))

# print(evenList)

# # # With Lambda
# # evenList = list(filter(lambda x: x % 2 == 0, numList))

# # print(evenList)


# # SEARCH 

# # word = ['Sands', 'Peace', 'Sandals', 'Birds', 'Dear']

# # numList = [1, 2, 3, 4, 5]
# # resInt = 2 in numList # True
# # resInt = 6 in numList # False

# # numString = 'You can jump'
# # resStr = 'You' in numString # True
# # resStr = 'you' in numString # False

# # print(resStr)


# # HOMEWORK #

# # Buat duplicate function untuk map dan filter
# numList = [1, 2, 3, 4, 5]
# def times2(num):
#     return num * 2

# def myMap(fun, lis):
#     mapList = []

#     for i in lis:
#         res = fun(i)
#         mapList.append(res)

#     return mapList

# myMapRes= myMap(times2, numList)
# print(numList)
# print(myMapRes)

# def myFilter(fun, lis):
    # do something

numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]

def even(num):
    return num % 2 == 0

def myFilter(fun, lis):
    # List kosong untuk menyimpan hasil filter
    filterList = []
    # Loop sebanyak data di List
    for i in lis:
        # Setiap loop akan return True / False, disimpan di 'res'
        res = fun(i)
        # Jika 'res' berisi True, maka nilai 'i' akan dimasukkan ke 'filterList'
        if res == True:
            filterList.append(i)
    # list yang berisi hasil filter, dikeluarkan dari 'myFilter'
    return filterList

myFilterRes = myFilter(even, numList)
print(numList)
print(myFilterRes)
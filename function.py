# Function
# Sekumpulan / block code yang dapat diberikan nama
# dan dapat digunakan berulang
# Dapat memiliki input, output, atau keduanya
 
#  Contoh function tidak menerima inputan apapun 
# def call():
#     print("Hello, neighbour")

# # Menerima satu input
# def greet(name):
#     print(f'Hello, (name)')

# # Menerima dua input
# def plus(x, y):
#     res = x + y
#     # memiliki satu output
#     # variabel yang ada di dalam function tidak dapat diakses di luar function
#     # kode setelah return tidak akan diproses
#     return res # output dari function plus()

# result = plus(2, 3)
# print(f'Nilai result: {result}')

# Default parameter
# def multiple(x, y = 3):
#     res = x * y
#     return res

# resMultiple = multiple(5,2)
# print(resMultiple)

# resMultiple = multiple(5) # manggil default parameter y = 3, 5*3 = 15
# print(resMultiple)

# Function dapat menerima function 
# def oneFun():
#     print('Hello, i\'am oneFun')

# def twoFun(fun):
#     fun()

# twoFun(oneFun)

# def threeFun(fun, x, y):
#     res = fun(x, y)
#     res = res + 2
#     print(f"Hasil akhir: {res}")

# def fourFun(a,b):
#     result = a*b
#     return result

# threeFun(fourFun, 2, 3)


# List

# Index dimulai dari 0
# days =['Sunday', 'Monday', 'Tuesday']
# fruits = ['Apple', 'Mango', 'Banana']

# print(days[1])
# print(fruits[2])

# def renderDays(data):
#     for i in data:
#         print(f'Today is {i}')

# renderDays(days)

#1
# buat sebuah function yang menerima list
# akan me-return hasil kali dua dari semua angka yang ada di dalam list
# function bersifat dinamis, bisa menerima isi yg lebih dr 4 input

# nilaiAwal = [1, 3, 5, 7]
# # hasilAkhir = [2, 6, 10, 14]


# def kaliDua(num):
#     for i in num:
#         result = num*2

# kaliDua(listNumber)

# print (hasilAkhir)

# my_list = [1, 3, 5, 7]

# def multiplyByTwo(data):
#     my_new_list = []
    
#     for i in data:
#         res = i * 2
#         my_new_list.append(res)
#     return my_new_list
# finalResult = multiplyByTwo(my_list)

# print(my_list)
# print(finalResult)



# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']
# buah[1] = 'Kelapa'
# print(buah)


# Sebuah function yang dapat memisahkan nilai genap dan ganjil
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[11, 22, 34, 41, 52, 63, 71, 86]
# [0, 2, 4, 6, 8, 10] [1, 3, 5, 7, 9]


# mixNumber = [11, 22, 34, 41, 52, 63, 71, 86] 

# def oddEven(mixNumber): 
#     ev_list = [] 
#     od_list = []
#     finalList = [] 
#     for i in mixNumber: 
#         if (i % 2 == 0): 
#             ev_list.append(i) 
#         else: 
#             od_list.append(i) 

#     finalList.append(ev_list)
#     finalList.append(od_list)
#     return finalList

# result = oddEven (mixNumber)
# print(result)

#######################################
# vowels = 'aiueo'
# searchWord = input('Put your word: ')

# def changeWord(word):

#     if word[0] in 'aiueo':
#         word = word + 'ay'
    
#     else:
#         word = word[1:] + word[0] + 'ay'

#     print(word)

# changeWord('apple')
# changeWord('banana')


###############################

# def pig_latin(word):
#     if word[0] in "aeiou":
#         return word + 'yay'
#     else:
#         return word[1:] + word[0] + 'ay'

# sentence = input("Enter a word: ")
# print(' '.join(pig_latin(word) for word in sentence.split()))


################################

# Reversed Sentence

def sentRev(word):
    
    word = word.split()
    word.reverse()
    word = ' '.join(word)

    print(word)

sentRev("Hello my friend")

###### Has 99


# def has99(lis):
#     idx = lis.index(9)
#     if lis [idx + 1] == 9:
#         return True
#     else:
#         return False

# print (has99([1, 9, 9]))
# print (has99([5, 9, 2, 9]))
# print (has99([9, 3, 9]))
# print (has99([7, 9, 9, 6]))


def has99(lis):
    idx = lis.index(9)
    return lis [idx + 1] == 9


print (has99([1, 9, 9]))
print (has99([5, 9, 2, 9]))
print (has99([9, 3, 9]))
print (has99([7, 9, 9, 6]))
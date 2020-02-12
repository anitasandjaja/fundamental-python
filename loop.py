# LOOP

# 1 WHILE LOOP

# number = 1

# while number <= 5:  # akan terus berjalan selama kondisi pada while bernilai TRUE
#   print(f'Halo, print ke-{number}')
#   number += 1

#################

# number = 1
# while number < 10:
#   print(f'Ganjil: {number}')
#   number +=2

# print ('##############')

# number = 0
# while number < 11:
#   print(f'Genap: {number}')
#   number +=2


# 2 FOR LOOP

# [0, 1, 2, 3, 4, 5]
# for i in range(6):
#   print(f"Angka {i}")

# [0, 2, 4, 6, 8]
# for i in range(0,9,2):
#     print(f"Angka {i}")

# [1, 3, 5, 7, 9]
# for i in range(1,10,2):
#     print(f"Angka {i}")


################################
# DRAWING

# Horizontal stars
# * * * * * 

# stars = ''

# for val in range(5):
#   stars += ' * '
# print(stars)

# Vertical stars
# *
# *
# *
# *
# *

# stars = ''

# for i in range(5):
#   stars += ' * \n'

# print(stars)

# Square stars
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# stars = ''
# row = 5

# for i in range(row):   # menentukan banyaknya baris
#     for j in range(row):  # menentukan banyaknya bintang per baris
#         stars += ' * '
#     stars +='\n'
# print (stars)

# draw stars triangle increment:
# *
# * *
# * * *
# * * * *
# * * * * *

# stars = ''
# row = 5
# for i in range(row):   # menentukan banyaknya baris
#     for j in range(i+1):  # menentukan banyaknya bintang per baris
#         stars += ' * '
#     stars +='\n'
# print (stars)

############################################

# draw stars triangle stars decrement:
# * * * * *
# * * * * 
# * * *
# * *
# * 

# stars = ''
# row = 5

# # list nya range 5 isinya dari 0 - 4 -> [0, 1, 2, 3, 4]
# for i in range(row):   # menentukan banyaknya baris
#     for j in range(row, i, -1):  # menentukan banyaknya bintang per baris [5, 4, 3, 2, 1]
#         stars += ' * '
#     stars += '\n'
# print (stars)



# print("-----------------------------------")


# for i in range(0, 5):
#     for j in range(5, i, -1):
#         print("* ", end="")
#     print()


##############################
# draw increment and decrement stars

stars = ''
row = 5

# list nya range 5 isinya dari 0 - 4 -> [0, 1, 2, 3, 4]
for i in range(row):   # menentukan banyaknya baris
    for j in range(row, i, -1):  # menentukan banyaknya bintang per baris [5, 4, 3, 2, 1]
        stars += ' * '
    stars += '\n'


for i in range(1, row):   # menentukan banyaknya baris
    for j in range(i + 1):  # menentukan banyaknya bintang per baris
        stars += ' * '
    stars +='\n'
print (stars)


# catatan looping

# print(list(range(5,0,-1)))
# print(list(range(5,1,-1)))
# print(list(range(5,2,-1)))
# print(list(range(5,3,-1)))
# print(list(range(5,4,-1)))

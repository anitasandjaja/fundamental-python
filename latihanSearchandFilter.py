# words = ['Merdeka', 'Hello', 'Hellos', 'Andi', 'Sohib', 'Kari ayam']
# keyword = input(f'{words}\nSearch : ')
# final = []

# for i in words:
#     # 'a' in 'Merdeka'
#     # res bernilai True / False
#     res = keyword.lower() in i.lower() 

#     if res == True:
#         final.append(i)

# print(final)


#########################################################################################

employee = [
    {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
    {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
    {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
]
for i in employee:
    # i = {"name", "gender", "hobbies"}
    # Jika gendernya male, tambahkan kata Mr.
    # Jika females tambahkan kata Mrs.
    if i["gender"] == 'male':
        i["name"] = 'Mr.' + i["name"]
    else:
        i["name"] = 'Mrs.' + i["name"]
    
    name = i["name"]
    hobbies = ", ".join(i["hobbies"])
    lenHobbies = len(i["hobbies"])
    
    print(
    f'{name} has {lenHobbies} hobbies, they are {hobbies}'
    )


# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"

# x = mySeparator.join(myDict)

# print(x)

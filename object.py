####################
# CLASS and OBJECT #
####################

# Hampir semua yang ada di dalam Python merupakan sebuah object
# Di dalam object akan memiliki properties dan methoda
# Property: variable yang ada di dalam object
# Method: function yang ada di dalam object

# Class merupakan sebuah blue print / cetakan untuk membuat object

class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
        self.pets = ['Molly','Kitten']
        self.job = {'position' : 'Manager'} 

    def greet(self, _time):
        print(f'Good {_time}, my name is {self.name}')

obj = Person('Karen', 28)
obj.name
obj.age
print(obj.__dict__) # {'name': 'Karen', 'age':28}
print(obj.__dict__["name"]) #'Karen'
obj.greet('evening')

# Obj merupakan sebuah object yang memiliki property dan method
# Property :
#       buatan : name, age
#       bawaan : __dict__

#
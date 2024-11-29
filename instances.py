import random

class Dog:
    info = "A furry little cute creature"


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name



dog1 = Dog("Fido")
dog2 = Dog("Milo")
dog3 = Dog("Chilly")
dog3.age = 2

print(dog1.name)
print(dog2.name)
print(dog3.name,dog3.age)


class Square:
    sides = 4

my_shape = Square()
my_shape.height = 10
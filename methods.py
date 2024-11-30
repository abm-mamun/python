import random

class Dog:
    info = "A furry little cute creature"


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")



dog1 = Dog("Fido")
dog2 = Dog("Milo")

dog1.bark()
dog2.bark()

class Square:
    sides = 4

    def __init__(self):
        self.height = 0

    def area(self):
        return self.height * self.height

my_shape = Square()
my_shape.height = 10

print(my_shape.area())
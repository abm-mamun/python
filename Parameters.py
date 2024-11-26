#Parameters are a way for us to pass some info into a function
#make a function where each time we run it, we could pass a new person's name
def hello(name):
    print(f"Hello {name}!")

hello("Bill")

#Having more than one parameter being passed into function

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(4,8)
add_numbers(7,3)

#Create a function that takes in a dog's age and name prints a sentence about the dog

def dog_info(age, dname):
    print(f"My dog's name is {dname} and it's {age} years old")

dog_info(2, "Tommy")
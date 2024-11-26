#With functions, we can pass in information via parameters
#But also pass out information with returning that information

#function that doubles a number
def double(number):
    return number * 2

new_number = double(5)

print(new_number)

#Create a function that returns a string in all capital

def caps(text):
    return text.upper()

print (caps("Nick"))

names = ['nick', 'jane', 'sara']

for name in names:
    print (caps(name))
#user_text = input('Enter some text: ')
#
#print(user_text.upper())

#Input from console always comes as string!

#user_number = input("What do you want to double?: ")

#print(int(user_number) * 2)

## Ask for some text, then prompt "Enter 1 to uppercase and 
# 2 to lowecase: " and either upper or lowercase it

user_text = input('Enter some text: ')

user_input = input('Enter 1 to uppercase and 2 to lowercase: ')

if user_input == "1":
    print(user_text.upper())

if user_input == "2":
    print(user_text.lower())


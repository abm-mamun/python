def has_remainder(number1, number2):
    
    remainder = number1 % number2

    if remainder == 0:
        print("No remainder")
    else:
        print(f'The remainder is {remainder}')

has_remainder(8,6)
print("before")

try:
    4 / 0
    #print(name)
except NameError:
    print("This was a name issue")
except ZeroDivisionError:
    print("can't divide by zero")
except:
    print("Something went wrong")

class CheeseError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("Thhe word has to have atleast one letter!")
    return word.upper()

print(upper_fun(""))
print("after") 
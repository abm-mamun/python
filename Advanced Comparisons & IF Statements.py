age = 7
height = 140

# and
if age >= 8 and height >= 135:
    print("You can ride!")
else:
    print("You can't ride")

# or
if age >= 17 or height >= 160:
    print("You can ride!")
else:
    print("You can't ride")

# elif
if height <120:
    print("You can't ride any rides :( ")
elif height < 135:
    print("You can ride level-1 rides.")
elif height < 200:
    print("You can ride any ride")
else:
    print("Too tall to ride the rides")

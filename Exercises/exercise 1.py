#Print the Sum of a Current Number and a Previous number

previous_num = 0

for i in range(1,11):
    x_sum = previous_num + 1
    print("Current Number ", i, "Previous Number ", previous_num, "Sum: ", x_sum)
    previous_num = i
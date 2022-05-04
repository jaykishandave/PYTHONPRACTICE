# Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 11]
numbers_y = [75, 65, 35, 75, 30]

first = numbers_x[0]
last = numbers_x[-1]


def same_last():
    if first == last:
        print("Both values are same")
    else:
        print("First value and last value is not same")


same_last()

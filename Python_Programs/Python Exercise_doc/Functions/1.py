# Write a program to find different aggregates (min, max, mean and median) value in existing list of numbers.  [5,
# 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]

number = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
length = len(number)
median_val = 1


def find_median(li, len_size):
    global median_val
    li.sort()
    if len_size % 2 != 0:
        median_val = li[int(len_size / 2)]
        return median_val
    median_val = (li[int((len_size - 1) / 2)] + li[int((len_size - 1) / 2)]) / 2
    return median_val


def mean_fun(li):
    size = len(li)
    addition = float(0)
    mean_val = 0
    for i in range(0, size):
        addition = li[i] + addition
        mean_val = addition / size
    print("mean value is :--", "%.2f" % mean_val)


def max_fun(li):
    size = len(li)
    temp = 0
    for i in range(0, size):
        if li[i] > temp:
            temp = li[i]

    print("Max value is:--", float(temp))


def min_fun(li):
    size = len(li)
    temp = 0
    for i in range(0, size):
        # print("Value of list", li[i], temp)
        if temp == 0:
            temp = li[i]
        elif li[i] < temp:
            temp = li[i]

    print("Min value is:--", float(temp))


print(find_median(number, length))

mean_fun(number)

max_fun(number)

min_fun(number)

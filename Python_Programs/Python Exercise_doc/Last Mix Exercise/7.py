# 7.	Write a program to generate two sorted arrays containing numbers between 0, 100. Find the median of the two
# sorted arrays.

number = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
length = len(number)
median_val = 1


def findMedian(li, len_size):
    global median_val
    li.sort()
    print("Sorted list is ", li)
    if len_size % 2 != 0:
        median_val = li[int(len_size / 2)]
        return median_val
    median_val = (li[int((len_size - 1) / 2)] + li[int((len_size - 1) / 2)]) / 2
    return median_val


print(findMedian(number, length))

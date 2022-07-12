"""Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second"""

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
l1_size = len(l1)
l2_size = len(l2)


def odev_val(li1, li2):
    for i in range(l1_size):
        if i % 2 == 0:
            l3.append(li1[i])
    for j in range(l2_size):
        if j % 2 != 0:
            l3.append(li2[j])
    print(l3)


odev_val(l1, l2)

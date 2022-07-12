"""Exercise 5: Iterate both lists simultaneously"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
size = len(list2)

for i, j in zip(list1, list2[::-1]):
    print(i, j)

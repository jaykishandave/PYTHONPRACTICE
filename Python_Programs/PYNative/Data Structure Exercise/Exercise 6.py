"""Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set"""

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
bar = first_set.copy()
for i in first_set:
    for j in second_set:
        if i == j:
            print(i)
            bar.remove(i)
print(bar)
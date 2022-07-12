# Exercise 8: Update set1 by adding items from set2, except common items

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

for i in set2:
    if i in set1:
        set1.remove(i)
    else:
        set1.add(i)
print(set1)

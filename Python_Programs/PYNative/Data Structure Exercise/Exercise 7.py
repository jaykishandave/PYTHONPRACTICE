"""Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set"""

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
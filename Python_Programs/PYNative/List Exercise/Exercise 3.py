"""Exercise 3: Turn every item of a list into its square"""

numbers = [1, 2, 3, 4, 5, 6, 7]
res =[]

for i in numbers:
    i = i ** 2
    res.append(i)
print(res)

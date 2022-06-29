"""Exercise 1A: Create a string made of the first, middle and last character"""

str1 = "James"
size = len(str1)

first = str1[0]
mid = size // 2

first = first + str1[mid]+ str1[size - 1]

print(first)

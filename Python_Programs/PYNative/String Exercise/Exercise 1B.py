"""Exercise 1B: Create a string made of the middle three characters"""

str1 = "JaSonAyyyy"
size = len(str1)
mid = size // 2

f = mid - 1
l = mid + 1

res = str1[f] + str1[mid] + str1[l]
print(res)

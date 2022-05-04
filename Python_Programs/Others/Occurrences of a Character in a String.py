# name = input("Please Enter Name:--")
# count = 0
# name1 = name
# for i in name:
#     for j in name1:
#         if j == i:
#             count = count + 1
#     print("char {0} is {1} available".format(i, count))
#     count = 0

# ======================

str = input("Please Enter Str:--")
str1 = input("Please Enter Str1:--")

size = len(str)
size1= len(str1)

count = 0
for i in range(len(str)):
    if str[i:i+len(str1)] == str1:
        count += 1
print(count)

# 2.	Write a program to find duplicate words and remove it from string. Output should have unique words in string.
name = input("Please Enter Name:--")
li = []
str1 = ""

st = name.split()
for i in st:
    if i not in li:
        li.append(i)
print(" ".join(li))

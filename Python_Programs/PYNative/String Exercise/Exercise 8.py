# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?".lower()
str2 = "USA".lower()
cnt = 0
x = str1.split()

for i in x:
    if str2 in i:
        cnt += 1
print(cnt)


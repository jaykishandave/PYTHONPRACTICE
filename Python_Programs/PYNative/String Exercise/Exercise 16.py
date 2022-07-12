# Exercise 16: Removal all characters from a string except integers

import re

str1 = 'I am 25 years and 10 months old'
size = len(str1)
n = 0
j = ""
for i in str1:
    if re.findall(r"\d", i):
        # j = j + i
        str1="".join(i)
        print(str1)
# str1 = str1.replace(str1, i)
# print(str2)

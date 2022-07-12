"""Exercise 17: Find words with both alphabets and numbers"""
import re

str1 = "Emma25 is Data scientist50 and AI Expert"


def alphanum(strval):
    new_strval = strval.split()
    for i in new_strval:
        if re.findall(r"[A-Za-z]", i) and re.findall(r"[0-9]",i):
            print(i)


alphanum(str1)

"""Exercise 18: Replace each special symbol with # in the following string"""
import re

str1 = '/*Jon is @developer & musician!!'


def str_spl(newstr):
    for i in newstr:
        if re.findall(r"\W", i):
            i = i.replace(i, "#")
        print(i,end="")


str_spl(str1)

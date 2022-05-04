"""1.	Write a program which accepts a number as an argument and prints an ascending triangle pattern containing character ‘*’. For example output of function pattern(5) should be following,
*
**
***
****
*****"""

num = int(input("Please Enter the no:--"))


def pattern_fun(no):
    sp = no - 1

    for i in range(0, no):
        for j in range(0, sp):
            print(" ", end="")
        sp = sp - 1
        for k in range(0, i+1 ):
            print("* ", end="")
        print("")


pattern_fun(num)

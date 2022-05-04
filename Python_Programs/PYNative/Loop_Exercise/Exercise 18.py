# Exercise 18: Print the following pattern

"""*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""

num = int(input("Please enter the start number:--"))


def pattern_fun(no):
    for i in range(0, no + 1):
        for j in range(0, i):
            print("*", end="")
        print("")
    for k in range(no, 0, -1):
        for l in range(1, k):
            print("*", end="")
        print("")


pattern_fun(num)

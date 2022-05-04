"""Exercise 2: Print the following pattern

Write a program to print the following number pattern using a loop.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

num = int(input("Please Enter the no:--"))


def pattern_fun(no):
    for i in range(1, no+1):
        for j in range(1, i+1):
            print(j,end="")
        print("\n")


pattern_fun(num)

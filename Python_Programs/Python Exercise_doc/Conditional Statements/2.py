# 2.	Write a program to find largest number from given 3 number

num1 = int(input("Enter the number1:--"))
num2 = int(input("Enter the number2:--"))
num3 = int(input("Enter the number3:--"))


def large_no_fun(no1, no2, no3):
    if no1 > no2 or no1 > no3:
        print(no1, " is largest Number")
    elif no2 > no3 or no2 > no1:
        print(no2, " is largest Number")
    else:
        print(no3, " is largest Number")


large_no_fun(num1, num2, num3)

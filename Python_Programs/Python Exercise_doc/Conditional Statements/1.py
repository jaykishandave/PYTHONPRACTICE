# 1.	Write a program to check whether number is positive or negative

try:
    num = int(input("Enter the number:--"))
except ValueError:
    print("Enter valid integer! Please try again ...")


def positive_negative_fun(no):
    if no > 0:
        print("Number is positive")
    else:
        print("Number Negative")


positive_negative_fun(num)

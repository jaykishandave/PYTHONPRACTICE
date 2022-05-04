# 3.	Write a program to perform basic mathematical operations based on user input with validation. User input
# should be 2 numbers and operation sign (+, -, *, /, //)

num1 = int(input("Enter the number1:--"))
num2 = int(input("Enter the number2:--"))


def large_no_fun(no1, no2):
    addition_val = 0
    mul_val = 1
    div_val = 1
    div_int_val = 1
    sub_val = 0
    if no1 > 0 and no2 > 0:
        addition_val = no1 + no2
        mul_val = no1 * no2
        div_val = no1 / no2
        div_int_val = no1 // no2
        sub_val = no1 - no2

        print("addition is:--", addition_val)
        print("multiplication is:--", mul_val)
        print("Div is:--", div_val)
        print("Div int value  is:--", div_int_val)
        print("Substraction is:--", sub_val)
    else:
        print("Please enter the valid number")


large_no_fun(num1, num2)

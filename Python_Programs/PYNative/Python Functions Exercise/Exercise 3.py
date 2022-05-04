# Exercise 3: Return multiple values from a function

# Write a program to create function calculation() such that it can accept two variables and calculate addition and
# subtraction. Also, it must return both addition and subtraction in a single

num1 = int(input("Please enter the number 1:--"))
num2 = int(input("Please enter the number 2:--"))


def calculation(no1, no2):
    add_ans = no1 + no2
    sub_ans = no1 - no2

    return add_ans, sub_ans


print(calculation(num1, num2))

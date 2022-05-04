# Exercise 4: Create a function with default argument

"""Write a program to create a function show_employee() using the following conditions.

    It should accept the employee’s name and salary and display both.
    If the salary is missing in the function call then assign default value 9000 to salary"""

name = input("Enter your name")
salary = input("Please enter the salary:--")


def show_employee(nm, sal=None):
    sal = 9000
    print("name is :--", nm, "and salary is ", sal)


# if salary == '':
#     show_employee(name)
# else:
show_employee(name, salary)

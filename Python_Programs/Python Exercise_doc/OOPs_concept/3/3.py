# Calculate the salary of restaurant workers based on their role using OOPs concept. Use below formulas for salary
# calculation.
# 1. Calculation of Chef's salary = Hourly wage * Number working hours*   Number of Working Days + basic
# salary 2. Calculation of Waiter's salary = Monthly wage + Tips * 0.05 + Basic Salary
# 3. Calculation of Cleaner's salary = monthly wage + Extra Working Hours * Extra Working Salary + Basic salary

from restaurant_salary import *

res = restaurant_salary()

while True:

    print("1: Chef's salary")
    print("2: Waiter's salary")
    print("3: Cleaner's salary")
    print("4: Exit")

    ch = int(input("Select operation: "))

    if ch == 4:
        print("TATA Good Bye Khatam.......")
        break
    if ch == 1:
        res.chef_salary_fun()
    elif ch == 2:
        res.waiter_salary_fun()
    elif ch == 3:
        res.chef_salary_fun()

    else:
        print("Invalid Input")

    another_entry = input("Would you like to continue? Y/N:--").upper()
    if another_entry == "Y":
        pass
    else:
        print("TATA Good Bye Khatam.......")
        break

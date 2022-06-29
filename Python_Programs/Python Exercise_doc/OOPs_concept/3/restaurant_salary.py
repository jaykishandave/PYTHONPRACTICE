import sys


class restaurant_salary:
    def chef_salary_fun(self):
        hourly_wage = int(input("Enter the Hourly wage:-"))
        number_working_hours = int(input("Enter the working hour between 0 -12:-"))
        number_of_working_days = int(input("Enter the working days between 0 -31:-"))
        basic_salary = int(input("Enter the basic Salary:-"))
        try:
            if hourly_wage > 0 and number_working_hours > 0 and number_of_working_days > 0 and basic_salary > 0:
                if number_working_hours <= 12:
                    if number_of_working_days <= 31:
                        chef_salary = hourly_wage * number_working_hours * number_of_working_days + basic_salary
                    else:
                        print("Please enter the value less than 31 for working days")
                else:
                    print("Please enter the value less than 12 for working hours")
            else:
                raise ValueError
        except ValueError:
            print("Enter valid integer value! Please try again ...")
            sys.exit()

        print(f"Salary of is {chef_salary}")

    def waiter_salary_fun(self):
        monthly_wage = int(input("Enter the Monthly Wages:-"))
        tips = int(input("Enter the tips:-"))
        basic_salary = int(input("Enter the basic Salary:-"))
        try:
            if monthly_wage > 0 and tips > 0 and basic_salary > 0:
                waiter_salary = monthly_wage + tips * 0.05 + basic_salary
            else:
                raise ValueError
        except ValueError:
            print("Enter valid integer value! Please try again ...")
            sys.exit()
        print("Salary of waiter is:-", waiter_salary)

    def Cleaner_salary_fun(self):
        monthly_wage = int(input("Enter the Monthly Wages:-"))
        extra_working_hours = int(input("Enter the working hours:-"))
        extra_working_sal = int(input("Enter the extra working sal:-"))
        basic_salary = int(input("Enter the basic Salary:-"))

        try:
            if monthly_wage > 0 and extra_working_hours > 0 and extra_working_sal > 0 and basic_salary > 0:
                cleaner_salary = monthly_wage + extra_working_hours * extra_working_sal + basic_salary
            else:
                raise ValueError
        except ValueError:
            print("Enter valid integer value! Please try again ...")
            sys.exit()
        print("Salary for cleaner is:-", cleaner_salary)

class restaurant_salary:
    def chef_salary_fun(self):
        hourly_wage = int(input("Enter the Hourly wage:-"))
        number_working_hours = int(input("Enter the working hour between 0 -12:-"))
        number_of_working_days = int(input("Enter the working days between 0 -31:-"))
        basic_salary = int(input("Enter the basic Salary:-"))

        chef_salary = hourly_wage * number_working_hours * number_of_working_days + basic_salary

        print("Salary of Chef_salary is:-", chef_salary)

    def waiter_salary_fun(self):
        monthly_wage = int(input("Enter the Monthly Wages:-"))
        tips = int(input("Enter the tips:-"))
        basic_salary = int(input("Enter the basic Salary:-"))

        waiter_salary = monthly_wage + tips * 0.05 + basic_salary
        print("Salary of waiter is:-", waiter_salary)

    def Cleaner_salary_fun(self):
        monthly_wage = int(input("Enter the Monthly Wages:-"))
        extra_working_hours = int(input("Enter the working hours:-"))
        extra_working_sal = int(input("Enter the extra working sal:-"))
        basic_salary = int(input("Enter the basic Salary:-"))

        cleaner_salary = monthly_wage + extra_working_hours * extra_working_sal + basic_salary

        print("Salary for cleaner is:-", cleaner_salary)

# 1.	Write a program to take Employee Id, Name, Salary and Designation from user then perform below operations.
# 1. Write Json data in json file.
# 2. Read Json data from the json file.
# Note:-  If file already exist then don't need to create file again, Use existing file and perform operations.

import json

name = input("Enter the name:--")
salary = input("Enter the salary:--")
designation = input("Enter the designation:--")

employee_data = {"emp_name": name,
                 "salary": salary,
                 "designation": designation
                 }
json_obj = json.dumps(employee_data, indent=4)
with open("data.json", "a+") as file:
    file.write(json_obj)
    file.seek(0)
    content = file.read()
    print(content)

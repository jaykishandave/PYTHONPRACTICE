import json
import re

with open("json_file.json", "r+") as file:
    json_obj = json.load(file)
    # print (json_obj["Employees"])

    # Print the list of employee name and salary whose name being started from "S"
    print("Print the list of employee name and salary whose name being started from 'S'")
    for i in json_obj["Employees"]:
        if re.search("[%S]", i["Employee Name"]):
            print("Employee Name:-", i["Employee Name"])
            print("Employee Salary:-", i["Employee Salary"])
    #     Print the list of employee name whose salary is less than 30000
    print("Print the list of employee name whose salary is less than 30000")
    for i in json_obj["Employees"]:
        if i["Employee Salary"] < 30000:
            print("Employee Name:-", i["Employee Name"])

        #     Print the list of employee name whose salary is less than 30000
    print("Print the list of employees (all details) whose age is between 25-45")
    for i in json_obj["Employees"]:
        if 25 < i["Employee Age"] < 45:
            print("Employee Name:-", i["Employee Name"])
            print("Employee Age:-", i["Employee Age"])
            print("Employee Salary:-", i["Employee Salary"])
            print("Programming Languages:-", i["Programming Languages"])

        #     Print the list of employee name who are have knowledge of Python and Java.
    print("Print the list of employee name who are have knowledge of Python and Java.")

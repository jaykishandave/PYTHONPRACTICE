# Exercise 10: Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

res = sample_dict.get("emp1", {}).get("name")
print(res)

if res == "Jhon":
    new_res=sample_dict["emp1"]["salary"] = 80000
print(sample_dict)


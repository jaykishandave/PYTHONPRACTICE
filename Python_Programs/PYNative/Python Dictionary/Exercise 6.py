# Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

res = {}

for i in keys:
    sample_dict.pop(i)
print(sample_dict)

# Exercise 4: Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys

import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w+") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")


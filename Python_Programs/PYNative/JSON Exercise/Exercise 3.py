# Exercise 3: PrettyPrint following JSON data

import json

sampleJson = {"key1": "value1", "key2": "value2"}

prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))

print(prettyPrintedJson)
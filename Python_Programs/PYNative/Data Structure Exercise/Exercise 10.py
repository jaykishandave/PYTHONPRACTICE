"""Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
new_sample_list = []

for i in sample_list:
    if i not in new_sample_list:
        new_sample_list.append(i)
print(new_sample_list)
max_val= max(new_sample_list)
min_val = min(new_sample_list)
print(max_val,min_val)
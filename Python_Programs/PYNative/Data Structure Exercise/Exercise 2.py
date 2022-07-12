"""Exercise 2: Remove and add item in a list"""

"""Write a program to remove the item present at index 4 and 
add it to the 2nd position and at the end of the list"""

sample_list = [34, 54, 67, 89, 11, 43, 94]
size = len(sample_list)
deleted_val = sample_list[4]
sample_list.pop(4)
sample_list.insert(2,deleted_val)
sample_list.insert(size,deleted_val)
print(deleted_val)
print(sample_list)

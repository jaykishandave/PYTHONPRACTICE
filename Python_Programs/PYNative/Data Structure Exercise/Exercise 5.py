"""Exercise 5: Create a Python set such that it shows the element from both lists in a pair"""

first_list = [2, 3, 4, 5, 6, 7, 8]
first_size = len(first_list)
second_list = [4, 9, 16, 25, 36, 49, 64]
sec_size = len(second_list)

merge_list=set(zip(first_list,second_list))

print(merge_list)

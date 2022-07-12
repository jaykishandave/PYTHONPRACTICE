"""Count the occurrence of each element from a list"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dir1 = {}

for i in sample_list:
    size = len(str(i))
    dir1[i] = size
print(dir1)

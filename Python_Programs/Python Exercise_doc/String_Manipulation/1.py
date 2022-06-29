# 1.	Write a program to take string from user and find duplicate characters in string with its count

name = input("Please Enter Name:--")
size = len(name)
count = 0
for i in range(size):
    for j in range(size):
        if name[j] == name[i]:
            count = count + 1
    if count > 1:

        print("char {0} is available for {1} times and its duplicated".format(name[i], count))
        # continue
    else:
        print("char {0} is available for {1} time only and not duplicated".format(name[i], count))
    count = 0

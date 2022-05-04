# 1.	Write a program to take string from user and find duplicate characters in string with its count

name = input("Please Enter Name:--")
count = 0
for i in name:
    for j in name:
        if j == i:
            count = count + 1
    if count > 1:

        print("char {0} is available for {1} times and its duplicated".format(i, count))
        # continue
    else:
        print("char {0} is available for {1} time only and not duplicated".format(i, count))
    count = 0

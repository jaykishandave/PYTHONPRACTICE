"""11.	Using Set comprehension generate two sets,
a.	Set-1 having all the numbers  divisible by  3
b.	Set-2  having all the numbers divisible by  7"""

set1 = set()
set2 = set()
set3 = set()

num = int(input("Enter the number:--"))


def set_val_fun(no):
    for i in range(1, no + 1):
        if i % 3 == 0:
            set1.add(i)

        if i % 7 == 0:
            set2.add(i)

    print("Values div by 3 for set 1 is:--", (sorted(set1)))
    print("Values div for 7 for set 2 is:--", (sorted(set2)))
    for j in set1:
        for k in set2:
            # print("new set is", j)
            # print("new set1 is", k)
            if j == k:
                set3.add(k)

    print("value of set -3 is :--", (sorted(set3)))


set_val_fun(num)

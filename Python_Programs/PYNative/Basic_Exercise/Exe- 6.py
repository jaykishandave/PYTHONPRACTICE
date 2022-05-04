# Exercise 6: Display numbers divisible by 5 from a list

lists = [10, 20, 33, 46, 55]
size = len(lists)
no = int(input("Enter the Number:- "))


def div_by_num():
    for i in range(size):
        if lists[i]% no == 0:
            print(lists[i])


div_by_num()

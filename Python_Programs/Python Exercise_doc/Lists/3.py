"""Write a program to sort numbers in descending order from existing list.
Input :-  [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
Output :-  [2020, 1010, 554, 121, 80, 26, 23, 22, 15, 12, 11, 4, 3]
Note :- Need to do program in both way (using built in function and without using built in function)."""

list1 = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
size = len(list1)
mul = 1


def sort_builtin_fun(li):
    li.sort()
    print("List in Ascending Order using built in function:", li)
    li.sort(reverse=True)
    print("List in Descending Order using built in function", li)


sort_builtin_fun(list1)


def sort_fun(li):
    for i in range(0, size):
        for j in range(0, size):
            if li[i] > li[j]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
    print("List in Descending Order without using built in function", li)


sort_fun(list1)

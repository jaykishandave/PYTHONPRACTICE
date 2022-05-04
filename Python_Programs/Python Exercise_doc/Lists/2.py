# Write a program to do product of specific value(N) given by user in list of string.

list1 = ['abcd', '11', 'ff', 'pp', '50', '13', '19', 'hh']
num = int(input("Enter the Number:--"))
mul = 1
size = len(list1)


def list_mul_fun(li, no):
    for i in range(0, size):
        isnum_val = li[i].isnumeric()
        if isnum_val:
            mul = int(li[i]) * 2
            li[i] = mul
    print(li)


list_mul_fun(list1, num)

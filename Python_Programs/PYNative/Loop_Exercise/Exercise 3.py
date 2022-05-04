# Exercise 3: Calculate the sum of all numbers from 1 to a given number

num = int(input("Please Enter the no:--"))


def sum_no_fun(no):
    sum_ans = 0
    for i in range(1, no + 1):
        sum_ans = sum_ans + i
    print(sum_ans)


sum_no_fun(num)

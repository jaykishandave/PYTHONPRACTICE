# Exercise 4: Write a program to print multiplication table of a given number

num = int(input("Please Enter the no:--"))


def multiplication_fun(no):
    table_ans = 1;
    for i in range(1, 11):
        table_ans = i * no
        print(table_ans)


multiplication_fun(num)

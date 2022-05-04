# Exercise 13: Find the factorial of a given number

num = int(input("Please enter the start number:--"))
fact = 1


def fact_fun(no):
    global fact
    for i in range(1, no + 1):
        fact = fact * i
    print(fact)


fact_fun(num)

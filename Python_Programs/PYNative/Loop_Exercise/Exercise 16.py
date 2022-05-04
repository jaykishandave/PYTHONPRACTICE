# Exercise 16: Calculate the cube of all numbers from 1 to a given number

num = int(input("Please enter the start number:--"))


def cube_fun(no):
    for i in range(1, no+1):
        ans = i ** 3
        print(ans)


cube_fun(num)

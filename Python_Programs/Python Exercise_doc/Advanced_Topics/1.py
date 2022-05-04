# 1.	Write a program to generate numbers which is divisible by 7 in 1 to 100 using generator.

num = int(input("Enter the number:--"))


def div_fun(no):
    if no < 0:
        for i in range(0, no):
            if i % 7 == 0:
                yield i
    else:
        print("Please Enter the number greater then zero")


print(list(div_fun(num)))

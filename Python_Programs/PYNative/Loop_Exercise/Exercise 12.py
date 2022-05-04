# Exercise 12: Display Fibonacci series up to 10 terms

num = int(input("Please enter the start number:--"))
f = 0
s = 1
sum_val = 0


def fibo_fun(no):
    global f, s, sum_val
    print(f, s, end=",")
    for i in range(0, no):
        sum_val = f + s
        print(sum_val, end=",")
        f = s
        s = sum_val




fibo_fun(num)

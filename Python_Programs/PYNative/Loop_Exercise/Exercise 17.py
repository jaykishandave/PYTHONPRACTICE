# Exercise 17: Find the sum of the series upto n terms

# 2 + 22 + 222 + 2222 + 22222 = 24690


num = int(input("Please enter the start number:--"))
ans_val = 0
start = 2


def sr_fun(no):
    global start, ans_val
    for i in range(0, no):
        print(start, end="+")
        ans_val = ans_val + start
        start = start * 10 + 2
    print(ans_val)


sr_fun(num)

num = int(input("Please enter the number:--"))
f = 0
s = 1


def fibo_fun(no):
    global f, s

    if no == 0:
        yield f
    elif no == 1:
        yield s
    else:
        for i in range(0, no):
            yield f
            fibo_val = f + s
            f = s
            s = fibo_val


print(list(fibo_fun(num)))

# Exercise 14: Reverse a given integer number

num = int(input("Please enter the start number:--"))
rev_val = 0


def rev_no_fun(no):
    global rev_val
    while no > 0:
        rem = no % 10
        rev_val = (rev_val * 10) + rem
        no = no // 10
    print(rev_val)


rev_no_fun(num)

# 3. Pelindrome number (true / False)

num = int(input("Please Enter the Number:--"))
reverse = 0


def pelin_fun(no):
    global reverse
    while no != 0:
        ans = no % 10
        reverse = reverse * 10 + ans
        no = no // 10

    if reverse == num:
        print("True")
    else:
        print("False")


pelin_fun(num)

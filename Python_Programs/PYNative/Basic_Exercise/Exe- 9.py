# Exercise 9: Check Palindrome Number

no = int(input("Enter the number:--"))

temp = no


def pelin_num(num):
    ans = 0
    while num > 0:
        new_num = num % 10
        ans = (ans * 10) + new_num
        num = num // 10

        print("answer is : --", ans)
    if temp == ans:
        print("Number is Pelindrome")
    else:
        print("Number is not Pelindrome")


pelin_num(no)

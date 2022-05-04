# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

no = int(input("Enter the Number:--"))


def num_rev(num):
    ans = 0

    while num > 0:
        temp = num % 10
        ans = (ans * 10) + temp
        num = num // 10
    print(ans)


num_rev(no)

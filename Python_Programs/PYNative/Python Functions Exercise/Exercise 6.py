"""Exercise 6: Create a recursive function

Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself, again and again."""

num = int(input("Enter the value:--"))

ans = 0


def rec_sum(no):
    global ans
    if no < 0:
        return
    else:
        ans = ans + no
        rec_sum(no - 1)
    return ans


res = rec_sum(num)
print(res)

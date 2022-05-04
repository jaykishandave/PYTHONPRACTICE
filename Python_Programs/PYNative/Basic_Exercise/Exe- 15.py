# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

nbase = int(input("Please enter the base:--"))
nexp = int(input("Please Enter the exponent"))


def exponent(base, exp):
    ans = 1
    for i in range(exp):
        ans = ans * base
        i.count
    print(ans)


exponent(nbase, nexp)

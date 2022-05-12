"""2.	A palindromic number reads the same both ways. The greatest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the smallest and the greatest palindrome made from the product of two 3-digit numbers."""

num1 = int(input("Please enter the start number1:--"))
num2 = int(input("Please enter the start number2:--"))

temp = 0
rev = 0


def product_pelindrome_fun(no1, no2):
    global rev, temp
    prod = no1 * no2
    temp = prod
    while temp != 0:
        ans = temp % 10
        rev = rev * 10 + ans
        temp = temp // 10
    if rev == prod:
        print("number", prod, "is greatest palindrome")
    else:
        print("Number is not palindrome")


product_pelindrome_fun(num1, num2)

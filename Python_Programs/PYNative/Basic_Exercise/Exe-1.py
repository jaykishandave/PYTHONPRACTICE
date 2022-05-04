# Calculate the multiplication and sum of two numbers
num1 = int(input("Please Enter Number - 1"))
num2 = int(input("Please Enter Number - 2"))


def mul_sum(num1, num2):
    mul = num1 * num2
    if mul >= 1000:
        return mul
    else:
        add = num1 + num2
        return add


result = mul_sum(num1, num2)
print("The result is", result)

"""2.	A palindromic number reads the same both ways. The greatest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99. Find the smallest and the greatest palindrome made from the product of two 3-digit
numbers. """

# num1 = int(input("Please enter the start number:--"))
# num2 = int(input("Please enter the end number:--"))

max_product = 0
min_product = 0

# for i in range(num1, num2):
#     for j in range(i, num2):
#         product = i * j
#         reverse = 0
#         number = product
#         while number != 0:
#             ans = number % 10
#             reverse = reverse * 10 + ans
#             number = number // 10
#         if product == reverse and product > max_product:
#             max_product = product
#         if min_product == 0:
#             min_product = product
#         if product == reverse and product < min_product:
#             min_product = product
# print(f"{max_product} is largest Palindrome number ")
# print(f"{min_product} is Smallest Palindrome number ")


no = int(input("Please enter the digit number:--"))

end_range = (10 ** no) - 1
start_range = 1 + end_range // 10
for i in range(start_range, end_range):
    for j in range(i, end_range):
        product = i * j
        reverse = 0
        number = product
        while number != 0:
            ans = number % 10
            reverse = reverse * 10 + ans
            number = number // 10
        if product == reverse and product > max_product:
            max_product = product
        if min_product == 0:
            min_product = product
        if product == reverse and product < min_product:
            min_product = product
print(f"{max_product} is largest Palindrome number ")
print(f"{min_product} is Smallest Palindrome number ")

# ================================================
# OUTPUT:
# Largest Palindrom number : 913 X 993 = 906609

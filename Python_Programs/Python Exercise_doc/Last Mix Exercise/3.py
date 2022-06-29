"""3.	Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order with first character of each word in capital. For example :
Input:  your name is xyz,
Output:  Xyz Is Name Your"""

try:
   string_val = str(input("Enter the String:--"))
except ValueError:
    print("Enter String Value! Please try again ...")

split_string = string_val.split()

size = len(split_string)

for i in range(size - 1, -1, -1):
    print(split_string[i].title(), end=" ")

# Exercise 1: Create a function in Python
#
# Write a program to create a function that takes two arguments, name and age, and print their value.

name = input("Please enter the name:--")
age = int(input("Please enter your age:--"))


def info_fun(nm, ag):
    print("my name is:--", nm)
    print("my age is:--", ag)


info_fun(name, age)

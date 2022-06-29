"""Exercise 7: Assign a different name to function and call it through the new name

Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using
the new name. """

a = input("Enter the name:--")
b = input("Enter the age:--")


def display_stud(name, age):
    print(f"name is {name} and age is {age}")


show_stud = display_stud
show_stud(a, b)

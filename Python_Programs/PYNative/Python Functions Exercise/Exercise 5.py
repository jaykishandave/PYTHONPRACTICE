"""Exercise 5: Create an inner function to calculate the addition in the following way

    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it"""

no1 = int(input("Enter the value a:--"))
no2 = int(input("Enter the value b:--"))

final_ans = 0


# outer function
def outer_fun(a, b):
    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5


result = outer_fun(no1, no2)
print(result)

outer_fun(no1, no2)

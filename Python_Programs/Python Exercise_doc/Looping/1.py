"""Write a program to do Sum of N series. N value should be entered by user.
Input :- Please enter number to get sum of N Series Output :- 5 Sum of 1 to 5 :- 15"""

num = int(input("Enter the number:--"))

# add_val = 0


def sum_fun(no):
    add_val = 0
    for i in range(1, no+1):
        add_val = add_val + i
    print(add_val)


sum_fun(num)

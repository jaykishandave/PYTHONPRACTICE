"""Write a program to do Sum of N series. N value should be entered by user.
Input :- Please enter number to get sum of N Series Output :- 5 Sum of 1 to 5 :- 15"""

try:
    num = int(input("Enter the number:--"))
except ValueError:
    print("Enter valid integer! Please try again ...")


def sum_fun(no):
    if no > 0:
        add_val = 0
        for i in range(1, no + 1):
            add_val = add_val + i
    else:
        print("Please Enter the ")
    print(add_val)


sum_fun(num)

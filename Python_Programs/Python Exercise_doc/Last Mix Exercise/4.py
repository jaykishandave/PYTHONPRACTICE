"""4.	Write a one line program which outputs the summation of cube of all the odd numbers from 0 to 300 using
lambda, map, reduce and filter concept. (Refer to https://www.python-course.eu/python3_lambda.php) """

try:
    num = int(input("Please enter the number:--"))
except ValueError:
    print("Enter valid integer! Please try again ...")
sum_val = 0


def sum_cube_fun(no):
    global sum_val
    no = no ** 3
    sum_val = sum_val + no
    return sum_val


cube_map = list(map(sum_cube_fun, (i for i in range(1, num, 2))))

print(max(cube_map))

# 10.	Use list comprehension to generate a tuple of two values (from 0 to 100), where square of one value is equal
# to cube of other value.

square_list = []
cube_list = []

li = []

num = int(input("Enter the number:--"))


def compare_fun(no):
    for i in range(0, no):
        square_val = i ** 2
        for j in range(0, no):
            cube_val = j ** 3

            if square_val == cube_val:
                print("Square of", i, "is:-", square_val, " and Cube of ", j, "is:--", cube_val)
                square_list.append(i)
                cube_list.append(j)

                # li.append(i)
                # li.append(j)
                #
                # t1 = tuple(li)
    size = len(square_list)

    nums = [(square_list[x], cube_list[x]) for x in range(0, size)]

    print(nums)


compare_fun(num)

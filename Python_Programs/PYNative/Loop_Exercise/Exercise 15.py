# Exercise 15: Use a loop to display elements from a given list present at odd index position

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
size = len(my_list)


def odd_position_fun(list1):
    for i in range(1, size, 2):
        print(list1[i])


odd_position_fun(my_list)

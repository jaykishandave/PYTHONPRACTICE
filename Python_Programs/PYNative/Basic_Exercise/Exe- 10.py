list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

size_list1 = len(list1)
size_list2 = len(list2)
result_list = []


def list_combination():
    for i in range(size_list1):
        if list2[i] % 2 == 0:
            result_list.append(list2[i])
        if list1[i] % 2 != 0:
            result_list.append(list1[i])
    print("New list is:--", result_list)


list_combination()

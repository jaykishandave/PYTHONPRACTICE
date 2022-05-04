"""Write a program to triples each integer present in list [55, 22, 77,44, 58, 90, 30, 72]
 which are even. Use Continue statement"""

list1 = [55, 22, 77, 44, 58, 90, 30, 72]
list2 = []
size = len(list1)
ans_val = 0


def even_triples_fun(l1):
    global ans_val
    for i in range(0, size, 2):
        ans_val = l1[i] ** 3
        list2.append(ans_val)
    print(list2)


even_triples_fun(list1)

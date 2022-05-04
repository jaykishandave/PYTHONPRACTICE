# 2. Program to seperate odd even numbers from the list
test_list =[22,99,55,88,10,5,3,11,77,2,22,23]

for i in test_list:
    if i % 2 == 0:
        print("Number {} is even".format(i))
    else:
        print("Number {} is odd".format(i))

# def odd_even(test_list):
#     for i in test_list:
#         if(i%2==0):
#             print("Number {} is even".format(i))
#         else:
#             print("Number {} is odd".format(i));
# print(odd_even(test_list))
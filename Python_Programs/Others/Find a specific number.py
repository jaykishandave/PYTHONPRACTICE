# Find a specific number exists in the list or not

test_list = [1, 56, 6, 55, 4];
no = int(input("Please enter the number for find : --"))
# if (no in test_list):
#     print("true number {} is exist".format(no));
# else:
#     print("False number {} is not exist".format(no));


for i in test_list:
    if (no == i):
        print("true number {} is exist".format(no))
    # else:
    #     print("False number {} is not exist".format(no))
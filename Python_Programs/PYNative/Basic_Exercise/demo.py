# """# li =[22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
# # li1 = []
# #
# # size = len(li)
# # temp =0
# #
# # for i in range(0,size):
# #     for j in range(0,size):
# #         if li[i] > li[j]:
# #             temp = li[i]
# #             li[i] = li[j]
# #             li[j] = temp
# # print(li)
# #
# #
# # =================================================================
#
#
# list1 = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
#
#
# def min_fun(li):
#     size = len(li)
#     temp = 0
#     for i in range(0, size):
#         # print("Value of list", li[i], temp)
#         if temp == 0:
#             temp = li[i]
#         elif li[i] < temp:
#             temp = li[i]
#
#     print("Min value is:--", float(temp))
#
#
# def max_fun(li):
#     size = len(li)
#     temp = 0
#     for i in range(0, size):
#         if li[i] > temp:
#             temp = li[i]
#
#     print("Max value is:--", float(temp))
#
#
# def mean_fun(li):
#     size = len(li)
#     addition = float(0)
#     mean_val = 0
#     for i in range(0, size):
#         addition = li[i] + addition
#         mean_val = addition / size
#     print("mean value is :--", "%.2f" % mean_val)
#
#
# def median_fun(li):
#     temp = 0
#     size = len(li)
#
#     for i in range(0, size):
#         for j in range(0, size):
#             if li[i] > li[j]:
#                 temp = li[i]
#                 li[i] = li[j]
#                 li[j] = temp
#     median_val = int(size / 2)
#     print("Median value is:--", li[median_val])
#
#
# median_fun(list1)
#
# mean_fun(list1)
#
# max_fun(list1)
#
# min_fun(list1)
# """
#
# # ===================================================
# """num = int(input("Please Enter the no:--"))
#
#
# def pattern_fun(no):
#     m=no
#     for i in range(0, no):
#         for j in (no,0,-1):
#             print("-", end="")
#
#         for k in range(0, i+1):
#             print("* ",end="")
#
#         print("")
#
#
# pattern_fun(num)
#
# ========================================================================"""
# """# MAP
#
#
# num = int(input("Please enter the number:--"))
# sum_val = 0
#
#
# def cube_sum_fun(no):
#     global sum_val
#
#     no = no ** 3
#     sum_val = sum_val + no
#     return sum_val
#
#
# # cube_map = list(map(cube_sum_fun, (i for i in range(1, num, 2))))
# cube_filter = list(filter(cube_sum_fun,(i for i in range(1, num, 2))))
#
# # print(cube_sum_fun(num))
# # print(max(cube_map))
# print(cube_filter)"""
#
# # ===============================================================================
#
# """num = int(input("Please enter the number:--"))
# f = 0
# s = 1
#
#
#
# def fibo_fun(no):
#     global f ,s
#     for i in range(no):
#         fibo_val = f + s
#         f = s
#         s = fibo_val
#         return fibo_val
#
# for i in range(0,num):
#     print(fibo_fun(i))"""
#
# # ===================================================================
#
# # list1 = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
# # size = len(list1)
# # median_val = 1
# #
# #
# # def median_fun(li, len_size):
# #     global median_val
# #     li.sort()
# #     if len_size % 2 != 0:
# #         median_val = li[int(len_size / 2)]
# #         print(median_val)
# #     else:
# #         median_val = (li[int((median_val - 1) / 2)] + li[int((median_val - 1) // 2)]) / 2
# #         print(median_val)
#
#
# # median_fun(list1, size)
#
# # number = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
# # length = len(number)
# # median_val = 1
# #
# #
# # def findMedian(li, len_size):
# #     global median_val
# #     li.sort()
# #     if len_size % 2 != 0:
# #         median_val = li[int(len_size / 2)]
# #         return median_val
# #     median_val = (li[int((len_size - 1) / 2)] + li[int((len_size - 1) / 2)]) / 2
# #     return median_val
# #
# #
# # print(findMedian(number, length))
# #  ============================================================================

import re

list_pass = []
invalid_pass = []


# password = input("Please enter the password:--")


# def pass_fun(lp, nvpl):
#     for i in range(0, 5):
#         pwd = input("Please enter the password:--")
#         # lp.append(pwd)
#         # get_val_lp = lp[i]
#         # pass_size = len(get_val_lp)
#         pass_size = len(pwd)
#         print(pass_size)
#
#         if 8 < pass_size < 12 and re.search("[a-z]", pwd) and re.search("[A-Z]", pwd) and re.search(
#                 "[0-9]", pwd) and re.search("[\w]", pwd):
#             lp.append(pwd)
#
#         else:
#             nvpl.append(pwd)
#     print("Valid Password list is:--", lp)
#     print("InValid Password list is:--", nvpl)
#
#
# pass_fun(list_pass, invalid_pass)



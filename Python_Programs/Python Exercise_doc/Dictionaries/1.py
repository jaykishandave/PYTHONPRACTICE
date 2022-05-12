"""Write a program to differentiate number from existing list based on its digit.
  Input:-
  [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
  Output:
  1-Digit numbers :- 2 3 1 4
  2-Digit numbers :- 44 55 33 66
  3-Digit numbers :- 111 121
  4-Digit numbers : 1010 8080 2020
"""

list1 = [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
list_size = len(list1)
size = 0
dict1 = {}

for i in range(list_size):
    size = len(str(list1[i]))
    dict1[list1[i]] = size

print(dict1)

#  Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *
# * * * *
# * * *
# * *
# *

no = int(input("Please enter the Number:--"))
for i in range(no):
    for j in range(no, i, -1):
        print("*",end=" ")
    print("\n")

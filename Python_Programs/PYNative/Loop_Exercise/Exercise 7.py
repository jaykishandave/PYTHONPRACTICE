"""Exercise 7: Print the following pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1"""

no = int(input("Please Enter the no:--"))
for i in range(0, no+1):
    for j in range(no-i, 0, -1):
        print(j,end="")
    print("\n")

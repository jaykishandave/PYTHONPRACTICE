# Exercise 8: Print the following pattern
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def loop():
    for i in range(6):
        for j in range(i):
            print(i,end="")
        print("\n")


loop()

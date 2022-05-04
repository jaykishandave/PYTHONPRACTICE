# Exercise 13: Print multiplication table form 1 to 10

no = int(input("Enter the number:--"))


def mul(number):
    multi = 1
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            multi = i * j
            print(multi, end=" ")
        print("\n")


mul(no)

# Exercise 11: Write a program to display all prime numbers within a range

source = int(input("Please enter the start number:--"))
destination = int(input("Please enter the end number:--"))
flag = 0


def prime_def(start, end):
    global flag

    for i in range(start, end):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


prime_def(source, destination)

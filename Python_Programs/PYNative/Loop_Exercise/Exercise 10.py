# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

num = int(input("Please enter the number:--"))


def done_fun(no):
    for i in range(no):
        print(i)
    else:
        print("Done")


done_fun(num)

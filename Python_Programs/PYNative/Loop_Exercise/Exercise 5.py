# Exercise 5: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]


def div_by_fun(no):
    for i in no:
        if i % 5 == 0:
            if i > 150:
                continue
            elif i > 500:
                break
            else:
                print(i)


div_by_fun(numbers)

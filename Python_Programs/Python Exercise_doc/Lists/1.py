# 1.	Write a program to differentiate even numbers and odd numbers from existing list. Then Print even number and
# odd numbers.
test_list = [1, 3, 4, 5, 6, 2, 10, 12, 55, 66, 99, 111, 180]
list_even = []
list_odd = []

for i in test_list:
    if i % 2 == 0:
        list_even.append(i)

    else:

        list_odd.append(i)
print("Even numbsers:--", list_even, end="")
print("Odd numbsers:--", list_odd, end="")

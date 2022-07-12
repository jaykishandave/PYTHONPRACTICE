# Exercise 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
no = int(input("Enter the number:--"))
cnt=0

for i in tuple1:
    if no == i:
        cnt += 1
print(cnt)

print(tuple1.count(no))
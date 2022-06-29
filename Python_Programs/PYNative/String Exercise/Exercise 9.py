# Exercise 9: Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
size = len(str1)
sum_ans = 0
# avg = 0
cnt = 0

for i in str1:
    if i.isdigit():
        sum_ans = sum_ans + int(i)
        cnt += 1
avg = sum_ans / cnt
print(f"Sum is:{sum_ans},and avg is {avg}")

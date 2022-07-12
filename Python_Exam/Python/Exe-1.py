# Write a program to do the sum of n series

num = int(input("Please Enter the Number:--"))

sum_val = 0
cnt=0


def sum_serise(no):
    global sum_val,cnt
    for i in range(1, no + 1):
        cnt+=1
        sum_val = sum_val + i
        if i<=4:
            print(f"{i}+",end="")
        else:
            print(f"{i}=",sum_val, end="")


sum_serise(num)

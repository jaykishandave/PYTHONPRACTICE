# 2. Take 3 Integer inputs from user and print the largest of 3 numbers

a = int(input("Please enter the first value"));
b = int(input("Please enter second value"));
c= int(input("Please enter Third value"));

def largest_number(a,b,c):
    if(a>b and a>c):
        print(str(a) + " is largest number");
    elif(b>a and b>c):
        print(str(b) + " is largest number");
    else:
        print(str(c) + " is largest number");

largest_number(a,b,c)

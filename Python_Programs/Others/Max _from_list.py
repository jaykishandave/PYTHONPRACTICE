# Iterate through a list to find max number among all

test_list = [1, 56, 6, 55, 4,100];
#no = int(input("Please enter the number for find : --"))

max=0;

for i in test_list:
    #print("Value of i is {}".format(i))
    if(i>max):
        max=i
print("Max value is {0}".format(max))

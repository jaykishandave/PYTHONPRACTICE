

name = input("Student name is")
maths = int(input("Enter the marks for maths:--"))
sci = int(input("Enter the marks for maths:--"))
ss = int(input("Enter the marks for maths:--"))
english = int(input("Enter the marks for maths:--"))
total = 0
per = 0.0

if maths > 50 and sci > 50 and ss > 50 and english > 50:
    print("invalid value")

total = maths + sci + ss + english
per = total / 4
print("Per is {}".format(per))
if maths < 18 and sci < 18 and ss < 18 and english < 18 or per < 35:
    print(name + "You got Fail")
elif 35 <= per < 60:
    print(name + "You got Second Class")
elif 60 <= per < 70:
    print(name + "You got First Class")
elif per >= 70:
    print(name + "You got Distinction Class")



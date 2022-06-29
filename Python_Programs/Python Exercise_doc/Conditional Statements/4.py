try:
    name = str(input("Student name is"))
    maths = int(input("Enter the marks for maths:--"))
    sci = int(input("Enter the marks for Science:--"))
    ss = int(input("Enter the marks for SS:--"))
    english = int(input("Enter the marks for English:--"))
except ValueError:
    print("Enter valid integer! Please try again ...")
total = 0
per = 0.0

if 0 < maths < 50 or 0 < sci < 50 or 0 < ss < 50 or 0 < english < 50:
    print("Please enter the value between 1 to 50")
else:
    if maths < 18 and sci < 18 and ss < 18 and english < 18 or per < 35:
        print(name + "You got Fail")
    elif 35 <= per < 60:
        print(name + "You got Second Class")
    elif 60 <= per < 70:
        print(name + "You got First Class")
    elif per >= 70:
        print(name + "You got Distinction Class")
    total = maths + sci + ss + english
    per = (total / 200) * 100
    print("Per is {}".format(per))
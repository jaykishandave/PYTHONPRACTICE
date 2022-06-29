# Create Calculator using OOPs concept which allows user to perform basic operations(Addition, Subtraction,
# Multiplication and Division)

class calculator(Exception):
    # def __init__(self):

    def add_fun(self, no1, no2):

        addition = no1 + no2
        print(a, "+", b, "=", addition)

    def sub_fun(self, no1, no2):

        substraction = no1 - no2
        print(a, "-", b, "=", substraction)

    def mul_fun(self, no1, no2):

        multiplication = no1 * no2
        print(a, "*", b, "=", multiplication)

    def div_fun(self, no1, no2):

        try:
            if no1 > 0 or no2 > 0:
                division = no1 / no2
                print(a, "/", b, "=", division)
            else:
                raise calculator()
        except (calculator, ZeroDivisionError) as ae:
            print("Can't divide with zero")


cal = calculator()
flag = False
while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    ch = input("Select operation: ")

    if ch == 5:
        print("TATA Good Bye.......")
        break
    if ch == "1":
        a = int(input("Enter the Value of a:--"))
        b = int(input("Enter the value of b:--"))
        cal.add_fun(a, b)
    elif ch == "2":
        a = int(input("Enter the Value of a:--"))
        b = int(input("Enter the value of b:--"))
        cal.sub_fun(a, b)
    elif ch == "3":
        a = int(input("Enter the Value of a:--"))
        b = int(input("Enter the value of b:--"))
        cal.mul_fun(a, b)
    elif ch == "4":
        a = int(input("Enter the Value of a:--"))
        b = int(input("Enter the value of b:--"))
        cal.div_fun(a, b)

    else:
        print("Invalid Input")

        while True:
            another_entry = input("Would you like to continue? Y/N:--").upper()
            if another_entry == "Y":
                pass
                break
            elif another_entry == "N":
                flag = True
                print("Thank you for using the services.......")
                break
            else:
                print("Please Enter the valid input.....")
        if flag:
            break

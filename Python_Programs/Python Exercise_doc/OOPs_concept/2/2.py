# Create banking application using OOPs concept and perform following operations:-
# 1. Account holder can deposit amount.
# 2. Account holder can withdraw amount.
# 3. Account holder can view total available balance.

from Bank_operation import *

bank_oper = bankoperation()
while True:

    print("1: Deposit")
    print("2: Withdraw")
    print("3: Balance Check")
    print("4: Exit")

    ch = int(input("Select operation: "))

    if ch == 4:
        print("TATA Good Bye.......")
        break
    if ch == 1:
        bank_oper.deposit_fun()
    elif ch == 2:
        bank_oper.withdraw_fun()
    elif ch == 3:
        bank_oper.balance_check_fun()

    else:
        print("Invalid Input")

    another_entry = input("Would you like to continue? Y/N:--").upper()
    if another_entry == "Y":
        pass
    else:
        print("TATA Good Bye.......")
        break

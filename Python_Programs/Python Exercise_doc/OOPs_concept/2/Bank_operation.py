class bankoperation:
    def __init__(self):
        self.bal = 0

    def balance_check_fun(self):
        print("Available Balance:", self.bal)

    def withdraw_fun(self):
        withdraw_amt = int(input("Please Enter the amount for Withdraw:-"))
        # global available_balance
        try:
            if self.bal > 0:
                if self.bal > withdraw_amt:
                    self.bal = self.bal - withdraw_amt
                    print("You have Withdraw ", withdraw_amt, "and now your available balance is:--", self.bal)
                else:
                    raise ArithmeticError
            else:
                raise ArithmeticError
        except ArithmeticError as ae:
            print(f"You have not sufficient balance your available balance is only {self.bal}")

    def deposit_fun(self):
        deposit_amt = int(input("Please Enter the amount for deposit:-"))
        self.bal = self.bal + deposit_amt
        print("You have deposited Amount ", deposit_amt, "and now your available balance is:--", self.bal)

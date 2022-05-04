# available_balance = 0


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
                    # available_balance = self.bal
                    # yield bal
                    print("You have Withdraw ", withdraw_amt, "and now your available balance is:--", self.bal)
            else:
                raise ArithmeticError
        except ArithmeticError as ae:
            print("You have not sufficient balance")

    def deposit_fun(self):
        deposit_amt = int(input("Please Enter the amount for deposit:-"))
        self.bal = self.bal + deposit_amt
        # available_balance = self.bal
        # yield bal
        print("You have deposited Amount ", deposit_amt, "and now your available balance is:--", self.bal)

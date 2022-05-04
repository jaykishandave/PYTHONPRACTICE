# Exercise 12: Calculate income tax for the given income by adhering to the below rules

amt = int(input("Enter the Amount"))


def tax_cal(amount):
    tax_calculation = 0
    first_ten = 10000
    first_per_cnt = first_ten * 0 / 100
    print("First ten", first_ten)
    second_ten = 10000
    sec_per_cnt = second_ten * 10 / 100
    print("sec_per_cnt", sec_per_cnt)
    remain = amount - first_ten - second_ten
    print("remaining", remain)
    remain_tax_cnt = remain * 20 / 100
    print("remaining tax calculation", remain_tax_cnt)
    tax_calculation = sec_per_cnt + remain_tax_cnt + first_per_cnt
    print(tax_calculation)


tax_cal(amt)

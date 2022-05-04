import re

list_pass = []
invalid_pass = []


password = input("Please enter the password:--")


def pass_fun(lp, nvpl):
    for i in range(0, 5):
        pwd = input("Please enter the password:--")
        # lp.append(pwd)
        # get_val_lp = lp[i]
        # pass_size = len(get_val_lp)
        pass_size = len(pwd)
        print(pass_size)

        if 8 < pass_size < 12 and re.search("[a-z]", pwd) and re.search("[A-Z]", pwd) and re.search(
                "[0-9]", pwd) and re.search("[\w]", pwd):
            lp.append(pwd)

        else:
            nvpl.append(pwd)
    print("Valid Password list is:--", lp)
    print("InValid Password list is:--", nvpl)


pass_fun(list_pass, invalid_pass)
# people = {}
# no = int(input("Enter your no for input:--"))
#
#
# for i in range(0, no):
#     name = input("Enter your name:--")
#     age_val = int(input("Enter your age :--"))
#     mobile = int(input("Enter your Mobile Number:--"))
#     email = input("Enter your Email:--")
#     mac = input("Enter your mac address:--")
#
#     people[name] = {}
#     people[name]["age"] = age_val
#     people[name]["mobile"] = mobile
#     people[name]["email"] = email
#     people[name]["mac"] = mac
# print(people)


import re

data = '''Jay,+919999999999,jay@xyz.com,11:22:33:44:55:66
Jatin,+918888888888,jatin@xyz.com,22:33:44:55:66:77
Keval,+917777777777,keval@xyz.com,33:44:55:66:77:88
Harshil,+911111111111,harshil@xyz.com,44:55:66:77:88:99
Priyanka,+912222222222,priyanka@xyz.com,55:66:77:88:99:00
Bhumika,+913333333333,bhumika@xyz.com,66:77:88:99:00:11'''

sp_data = data.split()
size = len(sp_data)
# print(size)
di1 = {}

for i in range(0, size):
    name = re.findall("^[A-Za-z]+", sp_data[i])
    other = re.findall(r"[\+]\w.+", sp_data[i])
    records = dict(zip(name, other))
    di1
    print(records)

# print(name)

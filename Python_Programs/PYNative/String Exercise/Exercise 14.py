# Exercise 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
cnt = 0
for i in str_list:
    if i == "":
        str_list.remove(i)
print(str_list)
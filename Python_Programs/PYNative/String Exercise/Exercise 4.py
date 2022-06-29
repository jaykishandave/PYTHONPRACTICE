# Exercise 4: Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
l_str = ""
c_str = ""
for i in str1:
    if i.islower():
        l_str = l_str + i
    else:
        c_str = c_str + i
new_str = l_str + c_str
print(new_str)

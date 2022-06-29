s1 = "Abc"
s2 = "Xyz"
size_s1 = len(s1)
size_s2 = len(s2)
str_one = ""
str_two=""
new_str=""

for i in range(0, size_s1):
    for j in range(size_s2-1, -1,-1):
        str_one = s1[i] + s2[j]
        str_two=str_one
        new_str = new_str + str_two
        # print(s2[j])
        size_s2 = size_s2 - 1
        break
    size_s1 = size_s1 + 1

print(new_str)

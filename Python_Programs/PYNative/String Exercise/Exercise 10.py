str1 = "Apple"
size = len(str1)
cnt = 0
dict_obj = dict()
for i in str1:
    count = str1.count(i)
    print(count)
    dict_obj[i] = count
print(dict_obj)

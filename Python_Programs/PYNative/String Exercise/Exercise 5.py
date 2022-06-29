# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0

for i in str1:
    if i.isalpha():
        char_count +=1
    elif i.isdigit():
        digit_count+=1
    else:
        symbol_count+=1
print(char_count,digit_count,symbol_count)

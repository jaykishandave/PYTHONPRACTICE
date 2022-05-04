# Write a program to print characters, words, digit and special characters with its occurrences from text file using
# regex.

import re

your_string = input("Enter your sentence:--")
total_chars = len(your_string)
nums = ""
chars = ""
special_char = ""
word = re.findall(r"[\w]+", your_string)
ncnt = 0
ccnt = 0
wc = len(word)
special_cnt = 0
spaces = 0

for i in your_string:
    if re.findall(r"[0-9]", i):
        ncnt += 1
        nums = nums + i
    elif re.findall(r"[A-Za-z]", i):
        ccnt += 1
        chars = chars + i
    elif re.findall(r"[^\s\w]", i):
        special_cnt += 1
        special_char = special_char + i
    elif re.findall(r"[\s]", i):
        spaces += 1

print("count of digits are :-", ncnt, "and these are:--", nums)
print("count of alphabets are :-", ccnt, "and these are:--", chars)
print("count of Special chars are :-", special_cnt, "and these are:--", special_char)
print("count of Spaces are :-", spaces)
print("count of Words are :-", wc, "and these are:--", word)
print("Total Numbers of characters are:--", total_chars)

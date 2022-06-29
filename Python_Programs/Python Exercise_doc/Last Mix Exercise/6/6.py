# 6.	Write a program read a text file and count number of words and new line characters from the file.
import re


with open("demo.txt", "r") as file:
    file_read = file.read()
    words = file_read.split()
    words_cnt = len(words)
print(f"Word count is {words_cnt}")
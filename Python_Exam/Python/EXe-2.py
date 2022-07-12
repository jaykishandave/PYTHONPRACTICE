from collections import Counter

str1 = "hello folks"
sample_dict = {}


# 2. Find the occurance of Each
def count_char(text):
    for i in range(len(text)):
        if len(text) == 0:
            break
        ch = text[0]
        # don't count frequency of spaces
        if ch == ' ' or ch == '\t':
            continue
        count = 1
        for j in range(1, len(text)):
            if ch == text[j]:
                count += 1
        # replace all other occurrences of the character
        # whose count is done, strip() is required for
        # scenario where first char is replaced and there is
        # space after that
        text = text.replace(ch, '').strip()
        # print(ch + " - ", count)
        sample_dict[ch] = count
    print(sample_dict)



count_char(str1)

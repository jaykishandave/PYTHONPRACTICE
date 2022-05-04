# palin = "kanak"
# size = len(palin)
# for i in range(size):
#     for j in range(size - 1, -1, -1):
#         str1 = palin[i]
#         print("for j",palin[j])
#     print(str1,end="")


def count_char(text):
    for i in range(len(text)):
        if len(text) == 0:
            break;
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
        text = text.replace(ch, '1').strip()
        print(ch + " - ", count)


count_char('jaayaayn')

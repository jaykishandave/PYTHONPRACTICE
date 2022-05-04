# Print characters from a string that are present at an even index number

word = input("Enter the word")


def even_pos(value):
    size = len(value)
    for i in range(0, size, 2):
        answer = value[i]
        print(answer)


even_pos(word)

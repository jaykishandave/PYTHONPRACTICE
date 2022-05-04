# Remove first n characters from a string

word = input(" Enter the word: - ")
no = int(input("Enter the number: - "))


def remove_first_n(words, value):
    size = len(words)
    for i in range(value, size):
        answer = words[i]
        print(answer, end="")


remove_first_n(word, no)

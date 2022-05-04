# Return the count of a given substring from a string

str_x = "Emma is good developer. Emma is a writer"
word = input("Enter the word to calculate counts")
split_word = str_x.split()
size = len(split_word)


def word_count(word_sub, words):
    count = 0
    print("From sub:--", word_sub)
    print("From split:--", words)

    for i in range(size):
        print("Words OF I is: - ", words[i])
        if word_sub == words[i]:
            count = count + 1
    print("Count is", count)


word_count(word, split_word)

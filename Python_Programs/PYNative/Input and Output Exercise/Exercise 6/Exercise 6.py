# Exercise 6: Write all content of a given file into a new file by skipping line number

with open("file1.txt", "r") as file_r:
    read_file = file_r.readlines()
    size = len(read_file)
with open("file2.txt", "w") as file_w:
    for i in range(size):
        if i == 4:
            continue
        else:
            file_w.write(read_file[i])

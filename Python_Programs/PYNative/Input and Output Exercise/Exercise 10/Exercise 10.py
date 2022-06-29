# Read line number 4 from the following file

with open("file1.txt", "r") as file:
    read_file = file.readlines()
    size = len(read_file)

    for i in range(size):
        if i == 3:
            print(read_file[i])

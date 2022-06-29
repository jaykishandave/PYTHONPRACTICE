with open("file1.txt", "r") as file:
    read_file = file.read()
    size = len(read_file)

    if size == 0:
        print("File is Empty")
    else:
        print("File is not Empty")
        print(read_file)

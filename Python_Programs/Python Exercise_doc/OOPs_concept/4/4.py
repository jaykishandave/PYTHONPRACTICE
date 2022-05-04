from Library_Management import *

lib = library_management_fun()
while True:

    print("1: Display Available Book")
    print("2: Lend a Book")
    print("3: Add a New Book")
    print("4: Return a Book")
    print("5: Exit")

    ch = int(input("Select operation: "))

    if ch == 5:
        print("TATA Good Bye Khatam.......")
        break
    if ch == 1:
        lib.display_fun()
    elif ch == 2:
        lib.lend_fun()
    elif ch == 3:
        lib.add_new_book_fun()
    elif ch == 4:
        lib.return_lend_book_fun()
    else:
        print("Invalid Input")

    another_entry = input("Would you like to continue? Y/N:--").upper()
    if another_entry == "Y":
        pass
    else:
        print("TATA Good Bye Khatam.......")
        break

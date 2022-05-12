class library_management_fun:
    def __init__(self):
        self.library = ["book1", "book2", "book3", "book4", "book5"]
        self.book_lend = []
        self.size_library = len(self.library)
        self.size_booklend = len(self.book_lend)

    def display_fun(self):
        print("Available Books are:--", self.library)

    def lend_fun(self):
        lend_book = input("Please select the book from the available book").lower()
        print("Available books are:--", self.library)
        for i in range(0, self.size_library):
            if self.library[i] == lend_book and self.size_library != 0:
                self.library.remove(lend_book)
                print("Success, You have lend the book:", lend_book)
                self.book_lend.append(lend_book)
            else:
                print("Please select the correct book....")
                break

    def add_new_book_fun(self):
        add_book = input("Please enter the book name to add in the list:--").lower()
        if add_book in self.library:
            print("You have entered the duplicated book,Please enter the correct book")
        else:
            self.library.append(add_book)
            print("Success, You have added new book:", add_book)
            print("Available books are:--", self.library)

    def return_lend_book_fun(self):
        return_book = input("Please enter the book name to return in the list:--").lower()
        for i in range(0, self.size_library):
            if self.library[i] != return_book and self.size_booklend == 0:
                print("Please return the correct book....")
                break
            elif self.size_booklend != 0:
                if self.book_lend[i] == return_book:
                    self.book_lend.remove(return_book)
                    print("Success, You have return your book:", return_book)
                    self.library.append(return_book)

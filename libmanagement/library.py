class Library():
    def __init__(self,list):
        self.books_list=list
        self.available_list=list[:]
        self.books_lent={} # key book , value - username

    def display_availablebooks(self):
        for books in self.available_list:
            print(books)

    def display_allbooks(self):
        for books in self.books_list:
            print(books)

    def lend_books(self, name, book):
        if book not in self.books_list:
            print("Incorrect book, please check the books list")
            return
        if book in self.available_list:
            self.books_lent.update({book:name})
            self.available_list.remove(book)
            print("You can take the book")
        else:
            print("The book is already taken by : "+self.books_lent[book])

    def return_book(self,book):
        del self.books_lent[book]
        self.available_list.append(book)




if __name__=="__main__":
    lib=Library(["Revolution","Roots","Trail","Outsider","War and Peace","Gambler"])
    print("Welcome to library. Enter an Option:")
    while True:
        print("1.Display available books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")
        print("Option Please : ")
        user_option=int(input())
        if user_option==1:
            lib.display_availablebooks()
        elif user_option==2:
            lib.display_allbooks()
        elif user_option==3:
            name=input("Please enter the username to lend a book : ")
            book=input("Please enter the name of the book : ")
            lib.lend_books(name,book)
        elif user_option==4:
            book=input("Please enter the username to return a book : ")
            lib.return_book(book)
        elif user_option==5:
            break
        else:
            print("Invalid enrty !! please enter a valid option (1-5) : ")

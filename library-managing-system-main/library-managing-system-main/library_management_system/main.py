class library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks
    
    def stupidFunction(self,name):
        print(f"\nyou are stupid {name}\n")

    def displayAvailableBooks(self):
        print("Books available in this library are:")
        for book in self.books:
            print("\t" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}")
            self.books.remove(bookName)
        else:
            print("this book is either not available or please wait till somebody returns it")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("book has been returned")


class student:
    def __init__(self) :
        self.bookList = []

    def requestBook(self):
        self.Book = input("enter the name of the book you want to torrow\n")
        return self.Book

    def returnBook(self):
        self.Book = input("enter the name of books you want to return\n")
        return self.Book

if __name__ == "__main__":
    centralLibrary = library(["Algorithms", "Django", "python notes", "javascript"])
    student1 = student()
    welcomeMSG = """
        welcome to central library
        please choose an option
        1. listing all the books
        2. Add/Request a book
        3. Return a book
        4. Exit the library
        5. stupid
        """
    print(welcomeMSG)
    while(True):
        
        a = int(input("enter a choice:"))

        if(a == 1):
            centralLibrary.displayAvailableBooks()
        elif(a == 2):
            centralLibrary.borrowBook(student1.requestBook())
        elif(a == 3):
            centralLibrary.returnBook(student1.returnBook())
        elif(a == 4):
            exit()
        elif(5 == 5):
            centralLibrary.stupidFunction(input("enter your name \t"))
        else:
            print("invalid choice")
